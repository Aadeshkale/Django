from django import forms

class EmpForm(forms.Form):
    name=forms.CharField(max_length=20)
    email=forms.EmailField(max_length=50)
    sal=forms.IntegerField(max_value=50000)
    company=forms.CharField(max_length=20) 