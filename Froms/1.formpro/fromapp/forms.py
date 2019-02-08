from django import forms

class EmpFrom(forms.Form):
    name=forms.CharField(max_length=20)
    email=forms.EmailField(max_length=50)
    mobile=forms.IntegerField(max_value=100000)
    sal=forms.IntegerField()
    address=forms.Textarea()
