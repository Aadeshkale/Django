from django import forms
class EmpForm(forms.Form):
    name=forms.CharField(max_length=20,
    widget=forms.TextInput(
        attrs={
            'placeholder':'Enter ur name',
            'class':'form-control text-center'
        }
    )
    )
    email=forms.EmailField(max_length=50,
    widget=forms.TextInput(
        attrs={
             'placeholder':'Enter ur Email',
             'class':'form-control text-center',   
         })
    ) 
    sal=forms.IntegerField(max_value=1000000,
    widget=forms.NumberInput(
        attrs={
            'placeholder':'Enter ur salary',
            'class':'form-control text-center'
         })
    )
    company=forms.CharField(max_length=20,
    widget=forms.TextInput(
        attrs={
            'placeholder':'Enter ur Company',
            'class':'form-control text-center',
        })
    )
    location=forms.CharField(max_length=20,
    widget=forms.TextInput(
        attrs={
            'placeholder':'Enter ur Location',
            'class':'form-control text-center',
         })
    )
