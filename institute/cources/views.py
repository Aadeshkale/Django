from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    msg='<h1 style="color:red ; text-align: center; ">Working Fine :)</h1>'
    return HttpResponse(msg)