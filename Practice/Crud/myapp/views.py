from django.shortcuts import render,redirect
from myapp.models import Emp
from myapp.forms import *
from django.http import HttpResponse
from django.contrib import messages
def index(request):
   return render(request,'index.html')
def insert(request):
    if request.method=="POST":
        myform=InsertForm(request.POST)
        if myform.is_valid():
            remail=request.POST.get('email')
            if Emp.objects.filter(email=remail):
                messages.success(request,'Email is already Registered')
                return redirect(insert)
            else:
                myform.save()
                messages.success(request,'Data inserted Successfully')
                return redirect(insert)
        else:
            return HttpResponse('Data not valid')

    else:
        myform=InsertForm()
        return render(request,'insert.html',{'myform':myform})      