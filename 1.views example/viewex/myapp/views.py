from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse('<h2>working fine :)</h2>')

def contact(request):
    return HttpResponse('''
        <h2>name:Aadesh kale</h2>
        <h3>email:aadeshkale619@gamil.com</h3>
        <h4>phone:8421686825</h4>
    
        ''')

def courses(request):
    return HttpResponse('''
        <h3>name:Aadesh kale</h3>
        <h3>email:aadeshkale619@gamil.com</h3>
        <h3>phone:8421686825</h3>
       
    ''')