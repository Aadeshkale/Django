from django import forms
class EmpFrom(forms.Form):
    name=forms.CharField(max_length=20,
    label="Enter Employee Name:",
    widget=forms.TextInput(
        attrs={
            'class':'form-control',
        }
    )
    )
    email=forms.EmailField(max_length=20,
    label="Enter Employee Email:",
    widget=forms.TextInput(
        attrs={
            'class':'form-control',
        }
    )
    )
    salary=forms.IntegerField(
    label="Enter Employee Email:",
    widget=forms.TextInput(
        attrs={
            'class':'form-control',
        }
    )
    )
    company=forms.CharField(max_length=20,
    label="Enter Employee company:",
    widget=forms.TextInput(
        attrs={
            'class':'form-control',
        }
    )
    )
