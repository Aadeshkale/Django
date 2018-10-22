from django import forms
from myapp.models import Reg 
class RegForm(forms.ModelForm):
    class Meta:
        model=Reg
        fields='__all__'
    name=forms.CharField(
        widget=forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':'Enter ur name',
        })
    )
    email=forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class':'form-control',
            'placeholder':'Enter ur email',
        })
    )    
    phone=forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'class':'form-control',
            'placeholder':'Enter ur phone',
        })
    )
    gen=[
        ('M','male'),
        ('F','female'),
    ]
    gender=forms.ChoiceField(
        choices=gen,
        widget=forms.RadioSelect(),
    )
    cun=[
        ('India','India'),
        ('Other','Other'),
    ]
    country=forms.ChoiceField(
       choices=cun, 
    )
