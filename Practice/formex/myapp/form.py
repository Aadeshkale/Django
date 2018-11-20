from django import forms
class Myform(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    id=forms.IntegerField()
    your_file=forms.FileField()
