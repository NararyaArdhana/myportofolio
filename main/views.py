from django.shortcuts import render
from main.models import Experience


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


def show_experience(request):
    context = {
        "name": "Muhammad Nararya Ardhana",
        "experience_list": Experience.objects.all(),
    }

    return render(request, "experience.html", context)