from django import forms 
class RegForm(forms.Form):
    name=forms.CharField(max_length=20,
    widget=forms.TextInput(attrs={
        'placeholder':'Enter ur name',
        'class':'form-control',
    })
    )
    email=forms.EmailField(max_length=50,
    widget=forms.EmailInput(attrs={
        'placeholder':'Enter ur Email',
        'class':'form-control',
    })
    )
    gen=[
        ('male','male'),
        ('female','female'),
        ('other','other'),
    ]
    gender=forms.ChoiceField(
        choices=gen,
        widget=forms.RadioSelect()
    )
    cou=[
        ('india','india'),
        ('other','other'),
    ]
    country=forms.ChoiceField(
        choices=cou,
    )