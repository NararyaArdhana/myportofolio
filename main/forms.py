from django.forms import ModelForm
from main.models import Education, Experience


class EducationForm(ModelForm):
    class Meta:
        model = Education
        fields = ["institution", "degree", "start_year", "end_year"]

class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = ["title","description","category","thumbnail","ended_at",]