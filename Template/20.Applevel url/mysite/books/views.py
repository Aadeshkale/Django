from django.shortcuts import render

def python(request):
    return render (request,'books/python.html')
def django(request):
    return render(request,'books/django.html')