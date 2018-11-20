from django.shortcuts import render
from django.http import HttpResponse
from myapp.forms import RegForm
from myapp.models import Reg
def index(request):
   if request.method=='POST':
       myform=RegForm(request.POST)
       if myform.is_valid():
            remail=request.POST.get('email')
            rname=request.POST.get('name')
            rgender=request.POST.get('gender')
            rcountry=request.POST.get('country')
            if Reg.objects.filter(email=remail):
                return HttpResponse('<h1>Email is already register</h1>')
            else:
                Reg.objects.create(
                    name=rname,
                    email=remail,
                    gender=rgender,
                    country=rcountry,
                )     
                return HttpResponse('<h1>Data added successfully :) </h1>')
       else:
           return HttpResponse('<h1>data is not valid</h1>')     
   else:
        myform=RegForm()
        return render(request,'index.html',{'myform':myform}) 