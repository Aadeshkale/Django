from django import forms
from multifapp.models import Reg

class RegForm(forms.Form,forms.ModelForm):
    class Meta:
        model=Reg
        fields=['name','email','mobile','address']

    gen=[
        ('M','male'),
        ('F','female'),
        ('O','other'),
    ]    
    gender=forms.ChoiceField(choices=gen,widget=forms.RadioSelect())

    cou=[
        ('india','India'),
        ('other','Other'),
    ]
    country=forms.ChoiceField(choices=cou)