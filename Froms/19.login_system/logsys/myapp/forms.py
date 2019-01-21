from django import forms

class Reg(forms.Form):
    name=forms.CharField(max_length=30,
    widget=forms.TextInput(attrs={
        'class':'from-control',
        'placeholder':'Enter ur name',
    })
    )
    email=forms.EmailField(max_length=200,
       widget=forms.EmailInput(attrs={
        'class':'from-control',
        'placeholder':'Enter ur email',
       })
    )  
    number=forms.CharField(max_length=10,
          widget=forms.TextInput(attrs={
        'class':'from-control',
        'placeholder':'Enter ur number',
        })
    )    
    address=forms.CharField(max_length=100,
    widget=forms.Textarea(attrs={
        'class':'from-control',
        'placeholder':'Enter ur address',
    })
    )
    password=forms.CharField(max_length=10,
    widget=forms.PasswordInput(attrs={
        'class':'from-control',
        'placeholder':'Enter ur password',
        
    })
    )