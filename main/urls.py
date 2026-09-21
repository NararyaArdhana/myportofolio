from django.urls import path
from main.views import (
    show_main,
    show_experience,
    show_education,
    add_education,
    add_experience,
    update_education,
    update_experience,
    get_education_json,
    delete_education,
    delete_experience,
)

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("experience/", show_experience, name="show_experience"),
    path("experience/add/", add_experience, name="add_experience"),
    path("experience/<uuid:experience_id>/update/",update_experience,name="update_experience"),
    path("experience/<uuid:experience_id>/delete/",delete_experience,name="delete_experience"), 
    path("education/", show_education, name="show_education"),
    path("education/add/", add_education, name="add_education"),
    path("education/<int:education_id>/update/",update_education,name="update_education"),
    path("api/education/", get_education_json, name="get_education_json"),
    path("education/<int:education_id>/delete/",delete_education,name="delete_education"),
]