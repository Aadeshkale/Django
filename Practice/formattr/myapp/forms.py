from django import forms
class Employee(forms.Form):
    name=forms.CharField(max_length=20,
    widget=forms.TextInput(attrs={
        'placeholder':'Enter ur name'
    })
    )
    email=forms.EmailField(max_length=50,
    widget=forms.EmailInput(attrs={
        'placeholder':'Enter ur email'
    })
    )
    uid=forms.IntegerField(max_value=4000,
    widget=forms.NumberInput(attrs={
        'placeholder':'Enter ur uid'
    })
    )
    gen=[
        ('Male','male'),
        ('Female','female'),
        ('Other','other'),
    ]
    gender=forms.ChoiceField(choices=gen,
    widget=forms.RadioSelect(),
    )
    cou=[
        ('India','india'),
        ('Other','other'),
    ]
    country=forms.ChoiceField(choices=cou)
      

