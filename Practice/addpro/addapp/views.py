from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,'index.html')

def add(request):
    num1=int(request.GET['no1'])
    num2=int(request.GET['no2'])
    res=num1+num2
    return HttpResponse(res)