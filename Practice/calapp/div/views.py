from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def div(request):
    return render(request,'div.html')

def op(request):
    num1=int(request.GET['no1'])
    num2=int(request.GET['no2'])
    res=num1/num2
    s="<h1>Division is:%s"%(str(res))
    return HttpResponse(s)
    
    

