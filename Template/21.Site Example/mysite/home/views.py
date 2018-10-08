from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def python(request):
    return render(request,'python.html')

def django(request):
    return render(request,'django.html')

def restapi(request):
    return render(request,'restapi.html')
