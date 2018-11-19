from django.shortcuts import render
from django.http import HttpResponse
def add(request):
    return render(request,'add.html')

def op(request):
    num1=int(request.GET['no1'])
    num2=int(request.GET['no2'])
    res=num1+num2
    s="<h1>Addition is: "+str(res)+"</h1>"
    return HttpResponse(s)