from django import forms
from valapp.models import Info
class Contact(forms.ModelForm):
    class Meta():
        model=Info
        fields=['name','email']

    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) < 4:
            raise forms.ValidationError("Not enough words!",code=name)
        return name
    
