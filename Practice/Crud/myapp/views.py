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

def display(request):
    data=Emp.objects.all()
    return render(request,'display.html',{'data':data})

def update(request):
    if request.method=="POST":
        myform=UpdateForm(request.POST)
        if myform.is_valid():
            rmail=request.POST.get('email')
            rcou=request.POST.get('country')
            if Emp.objects.filter(email=rmail):
                ob=Emp.objects.filter(email=rmail)
                ob.update(country=rcou)
                messages.success(request,'Data updated sucessfully')
                return redirect(update)
            else:
                messages.success(request,'Email is not registered')
                return redirect(update)
        else:
              messages.success(request,'Data is invalid')
              return redirect(update)       
    else:
        myform=UpdateForm()
        return render(request,'update.html',{'myform':myform})          