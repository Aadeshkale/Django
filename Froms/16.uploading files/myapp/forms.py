from django import forms
from myapp.models import File
class FileForm(forms.ModelForm):
    class Meta():
        model=File
        fields='__all__'
        name=forms.CharField(max_length=50,
            widget=forms.TextInput(
                attrs={
                    'placeholder':'Enter name for File',
                    'class':"form-control",
                    }
            )
        )
        document=forms.FileField(
            widget=forms.FileInput(
                attrs={
                    'class':"custom-file-input mt-5",
                    'placeholder':'Choose File',
                }
            )
        )