from django import forms
from myapp.models import Reg
class RegForm(forms.ModelForm):
    class Meta():
        model=Reg,
        fields='__all__'
        
    name=forms.CharField(max_length=20,
    widget=forms.TextInput(
        attrs={
            'placeholder':'Enter ur name',
        }
    )
    )
    email=forms.EmailField(max_length=20,
    widget=forms.EmailInput(
        attrs={
            'placeholder':'Enter ur email',
        }
    )
    )
    gen=[
        ('Male','m'),
        ('Female','f'),
    ]
    gender=forms.ChoiceField(choices=gen,
    widget=forms.RadioSelect()
    )
    cou=[
        ('India','In'),
        ('Other','O'),
    ]
    country=forms.ChoiceField(choices=cou,
    )
