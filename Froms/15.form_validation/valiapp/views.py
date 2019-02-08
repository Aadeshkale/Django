from django.shortcuts import render
from valiapp.forms import Contact
from valiapp.models import Info
from django.http import HttpResponse
def index(request):
    if request.method=="POST":
        myform=Contact(request.POST)
        if myform.is_valid():
            return HttpResponse('Data is valid')
        else:
            pass            
    else:
        myform=Contact()
    return render(request,'index.html',{'myform':myform}) 
    