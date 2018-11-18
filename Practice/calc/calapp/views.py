from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,'index.html')

def add(request):
    return render(request,'add.html')

def sub(request):
    return render(request,'sub.html')

def mul(request):
    return render(request,'mul.html')

def div(request):
    return render(request,'div.html')

def addop(request):
    x=int(request.GET['no1'])
    y=int(request.GET['no2'])
    z=x+y
    s="your Addition is:",z
    return HttpResponse(s)


def subop(request):
    x=int(request.GET['no1'])
    y=int(request.GET['no2'])
    z=x-y
    s="your Substration is:",z
    return HttpResponse(s)


def mulop(request):
    x=int(request.GET['no1'])
    y=int(request.GET['no2'])
    z=x*y
    s="your Multiplication is:",z
    return HttpResponse(s)


def divop(request):
    x=int(request.GET['no1'])
    y=int(request.GET['no2'])
    z=x//y
    s="your Division is:",z
    return HttpResponse(s)

