from django import forms
class CalForm(forms.Form):
    no1=forms.IntegerField()
    no2=forms.IntegerField()