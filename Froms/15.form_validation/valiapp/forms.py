from django import forms
from valiapp.models import Info
import re
class Contact(forms.ModelForm):
    class Meta():
        model=Info
        fields="__all__"

    name=forms.CharField(max_length=30,
    widget=forms.TextInput(attrs={
        'placeholder':'Enter your name',
        'class':'form-control',
    })
    ) 
    email=forms.EmailField(max_length=70,
    widget=forms.EmailInput(attrs={
        'placeholder':'Enter your email',
        'class':'form-control',
    })
    )
    phone=forms.CharField(max_length=10,
    widget=forms.TextInput(attrs={
        'placeholder':'Enter your mobile no',
        'class':'form-control',    
    })
    )
    gen=[
        ('Male','Male'),
        ('Female','Female'),
        ('Other','Other'),
    ]
    gender=forms.ChoiceField(choices=gen,
    widget=forms.RadioSelect(),
    )
    cou=[
        ('India','India'),
        ('Other','Other'),
    ]
    country=forms.ChoiceField(choices=cou)

    def clean_name(self):
        name=self.cleaned_data['name']
        if len(name)<5:
            raise forms.ValidationError('Please enter valid name')    
        return name

    def clean_email(self):
        email=self.cleaned_data['email']
        if not re.match(r'^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$',email):
            raise forms.ValidationError('Please enter valid email address',code='email')
        return email

    def clean_phone(self):
        phone=self.cleaned_data['phone']
        if not re.match(r'^[7-9][0-9]{9}$',phone):
            raise forms.ValidationError('Please Enter valid phone no')
        return phone





