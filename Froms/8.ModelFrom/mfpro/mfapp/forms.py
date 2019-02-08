from django import forms
from mfapp.models import Stu
class StuForm(forms.ModelForm):
    class Meta():
        model = Stu
        fields=['name','location','age']