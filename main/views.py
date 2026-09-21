from django.shortcuts import render, redirect,get_object_or_404
from main.models import Experience, Education
from main.forms import EducationForm
from django.core import serializers
from django.http import HttpResponse


def show_main(request):
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
    }

    return render(request, "index.html", context)

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
    context = {
        "name": "Muhammad Nararya Ardhana",
        "experience_list": Experience.objects.all(),
    }

    return render(request, "experience.html", context)

def add_education(request):
    form = EducationForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("main:show_education")

    context = {
        "name": "Muhammad Nararya Ardhana",
        "form": form,
    }

    return render(request, "add_education.html", context)

def update_education(request, education_id):
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

def delete_education(request, education_id):
    education = get_object_or_404(Education, pk=education_id)

    if request.method == "POST":
        education.delete()
        return redirect("main:show_education")

    return redirect("main:show_education")