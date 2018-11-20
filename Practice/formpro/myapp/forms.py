from django import forms
class Employee(forms.Form):
    name=forms.CharField(max_length=20)
    email=forms.EmailField(max_length=50)
    gen=[
        ('Male',"Male"),
        ('Female',"Female"),
    ]
    gender=forms.ChoiceField(choices=gen,
    widget=forms.RadioSelect(),
    )
    uid=forms.IntegerField()
