from django import forms
from django.core.validators import RegexValidator
class ValForm(forms.Form):
    name=forms.CharField(max_length=20,
    widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Enter ur name',
    })    
    )
    email=forms.CharField(max_length=54,
    validators=[RegexValidator(regex=r'^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$',message="Enter valid Email address")],
    widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Enter ur Email',
    })
    )
    number=forms.CharField(max_length=10,
    widget=forms.NumberInput(attrs={
        'class':'form-control',
        'placeholder':'Enter ur number',
    })
    )