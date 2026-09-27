from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from main.models import Education, Experience
from django.contrib.auth.forms import AuthenticationForm


class EducationForm(ModelForm):
    class Meta:
        model = Education
        fields = ["institution", "degree", "start_year", "end_year"]

class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = ["title","description","category","thumbnail","ended_at",]

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]