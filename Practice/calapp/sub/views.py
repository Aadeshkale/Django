from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def sub(request):
    return render(request,'sub.html')

def op(request):
    num1=int(request.GET['no1'])
    num2=int(request.GET['no2'])
    res=num1-   num2
    s="<h1> Substarction is:"+ str(res) +"</h1>"
    return HttpResponse(s)