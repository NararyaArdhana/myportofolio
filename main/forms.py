from django.forms import ModelForm
from django.core.exceptions import ValidationError
from django.utils.html import strip_tags

from main.models import Education, Experience
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class EducationForm(ModelForm):
    class Meta:
        model = Education
        fields = ["institution", "degree", "start_year", "end_year"]

class ExperienceForm(ModelForm):

    class Meta:
        model = Experience
        fields = [
            "title",
            "description",
            "category",
            "thumbnail",
            "ended_at",
        ]

    def clean_title(self):
        title = self.cleaned_data["title"]

        if strip_tags(title) != title:
            raise ValidationError(
                "Title tidak boleh mengandung HTML."
            )

        return title

    def clean_description(self):
        description = self.cleaned_data["description"]

        if strip_tags(description) != description:
            raise ValidationError(
                "Description tidak boleh mengandung HTML."
            )

        return description

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]