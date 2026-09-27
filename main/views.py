import datetime
from django.shortcuts import render, redirect,get_object_or_404
from main.models import Experience, Education
from main.forms import EducationForm, ExperienceForm, RegisterForm,AuthenticationForm
from django.core import serializers
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied


def show_main(request):

    last_login = request.COOKIES.get(
        "last_login",
        "Belum ada sesi login / Cookie tidak ditemukan"
    )

    context = {
        "name": "Muhammad Nararya Ardhana",
        "npm": "2506657094",
        "study_program": "S1 Ilmu Komputer",
        "bio": (
            "Computer science student with a strong interest in technology "
            "and business development. Skilled in teamwork, time management, "
            "and problem-solving. Passionate about continuous learning and "
            "contributing to innovative technology solutions."
        ),
        "last_login": last_login,
    }

    return render(request, "index.html", context)

def register(request):
    form = RegisterForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("main:show_main")

    context = {
        "name": "Muhammad Nararya Ardhana",
        "form": form,
    }

    return render(request, "register.html", context)


def login_user(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)

        response = redirect("main:show_main")
        response.set_cookie(
            "last_login",
            datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )

        return response

    context = {
        "name": "Muhammad Nararya Ardhana",
        "form": form,
    }

    return render(request, "login.html", context)


def logout_user(request):
    logout(request)

    response = redirect("main:show_main")
    response.delete_cookie("last_login")

    return response

def show_education(request):
    json_response = get_education_json(request)

    education = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )

    education = [item.object for item in education]

    institution_query = request.GET.get("institution", "").strip()

    context = {
        "name": "Muhammad Nararya Ardhana",
        "education_list": education,
        "institution_query": institution_query,
    }

    return render(request, "education.html", context)


def show_experience(request):
    json_response = get_experience_json(request)

    experience = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )

    experience = [item.object for item in experience]

    context = {
        "name": "Muhammad Nararya Ardhana",
        "experience_list": experience,
    }

    return render(request, "experience.html", context)

@login_required(login_url="/login/")
def add_education(request):
    if not request.user.is_superuser:
        raise PermissionDenied

    form = EducationForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("main:show_education")

    context = {
        "name": "Muhammad Nararya Ardhana",
        "form": form,
    }

    return render(request, "education_form.html", context)

@login_required(login_url="/login/")
def add_experience(request):
    if not request.user.is_superuser:
        raise PermissionDenied
    
    form = ExperienceForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("main:show_experience")

    context = {
        "name": "Muhammad Nararya Ardhana",
        "form": form,
    }

    return render(request, "add_experience.html", context)

@login_required(login_url="/login/")
def update_education(request, education_id):

    if not request.user.is_superuser:
        raise PermissionDenied
    
    education = get_object_or_404(Education, pk=education_id)
    form = EducationForm(request.POST or None, instance=education)

    if form.is_valid():
        form.save()
        return redirect("main:show_education")

    context = {
        "name": "Muhammad Nararya Ardhana",
        "form": form,
        "education": education,
    }

    return render(request, "update_education.html", context)

@login_required(login_url="/login/")
def update_experience(request, experience_id):
    if not request.user.is_superuser:
        raise PermissionDenied
    
    experience = get_object_or_404(Experience, pk=experience_id)
    form = ExperienceForm(request.POST or None, instance=experience)

    if form.is_valid():
        form.save()
        return redirect("main:show_experience")

    context = {
        "name": "Muhammad Nararya Ardhana",
        "form": form,
        "experience": experience,
    }

    return render(request, "update_experience.html", context)

def get_education_json(request):
    institution_query = request.GET.get("institution", "").strip()
    education = Education.objects.all()

    if institution_query:
        education = education.filter(
            institution__icontains=institution_query
        )

    education_json = serializers.serialize("json", education)

    return HttpResponse(
        education_json,
        content_type="application/json"
    )

def get_experience_json(request):
    title_query = request.GET.get("title", "").strip()

    experiences = Experience.objects.all()

    if title_query:
        experiences = experiences.filter(
            title__icontains=title_query
        )

    experiences_json = serializers.serialize(
        "json",
        experiences
    )

    return HttpResponse(
        experiences_json,
        content_type="application/json"
    )

@login_required(login_url="/login/")
def delete_education(request, education_id):
    if not request.user.is_superuser:
        raise PermissionDenied
    
    education = get_object_or_404(Education, pk=education_id)

    if request.method == "POST":
        education.delete()
        return redirect("main:show_education")

    return redirect("main:show_education")

@login_required(login_url="/login/")
def delete_experience(request, experience_id):
    if not request.user.is_superuser:
        raise PermissionDenied
    
    experience = get_object_or_404(Experience, pk=experience_id)

    if request.method == "POST":
        experience.delete()
        return redirect("main:show_experience")

    return redirect("main:show_experience")