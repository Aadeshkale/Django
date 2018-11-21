from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def add(request):
    response=render(request,'index.html')
    response.set_cookie('color','red')
    return response

def remove(request):
    response