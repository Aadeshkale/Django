from django import forms

class RegForm(forms.Form):
    Name=forms.CharField(max_length=20,
    widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder':'Enter ur name',
        })
    )
    Email=forms.EmailField(max_length=50,
    widget=forms.EmailInput(attrs={
        'class':'form-control',
        'placeholder':'Enter ur email',
    })
    )
    Age=forms.IntegerField(max_value=100,
    widget=forms.NumberInput(attrs={
        'class':'form-control',
        'placeholder':'Enter ur age',
    })
    )

    Address=forms.CharField(max_length=50,
    widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder':'Enter ur address',
        })
    )