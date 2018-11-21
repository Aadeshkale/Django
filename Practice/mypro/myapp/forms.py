from django import forms
from myapp.models import Reg
class RegForm(forms.ModelForm):
    class Meta():
        model=Reg
        fields='__all__'
        
    name=forms.CharField(max_length=20,
    widget=forms.TextInput(
        attrs={
            'placeholder':'Enter ur name',
            'class':'form-control',
        }
    )
    )
    email=forms.EmailField(max_length=20,
    widget=forms.EmailInput(
        attrs={
            'placeholder':'Enter ur email',
            'class':'form-control',
        }
    )
    )
    gen=[
        ('Male','male'),
        ('Female','female'),
    ]
    gender=forms.ChoiceField(choices=gen,
    widget=forms.RadioSelect(
        attrs={
            'class':'custom-radio',
        }
    )
    )
    cou=[
        ('India','India'),
        ('Other','Other'),
    ]
    country=forms.ChoiceField(choices=cou,
    )
