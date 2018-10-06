from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,'Addapp/add.html')

def addfun(request):
    x=int(request.GET['val1'])
    y=int(request.GET['val2'])
    z=x+y;
    s="your Addition is:",z
    return HttpResponse(s)
