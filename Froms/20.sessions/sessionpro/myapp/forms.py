from django import forms

class LoginForm(forms.Form):
    username=forms.CharField(max_length=70,
    widget=forms.TextInput(attrs={
        'label':'Enter ur username',
        'class':'text-left form-control',
    })
    )
    password=forms.CharField(max_length=70,
    widget=forms.PasswordInput(attrs={
        'label':'Enter ur password',
        'class':'form-control',
    })
    )