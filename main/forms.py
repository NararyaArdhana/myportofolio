from django.forms import ModelForm
from main.models import Education


class EducationForm(ModelForm):
    class Meta:
        model = Education
        fields = ["institution", "degree", "start_year", "end_year"]