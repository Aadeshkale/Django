from django.shortcuts import render,redirect
from myapp.forms import Reg
from django.contrib.auth.models import User
from django.contrib import messages


def index(request):
    return render(request,'index.html')

def register(request):
    if request.method=="POST":
       myform=Reg(request.POST)
       if myform.is_valid():
          username=request.POST['name']
          email=request.POST['email']
          password=request.POST['password']
          if User.objects.filter(username=email):
              messages.success(request,'User is already registered :)')
          else:
               ob=User.objects.create_user(username=email,password=password,email=email)
               ob.is_staff=True
               ob.is_superuser=True
               ob.save()
               messages.success(request,'User registered successfully :)')
          return redirect(index)
       else:
           messages.success(request,'data is Invalid :(')
           return redirect(index)          
    else:
        myform=Reg()
        return render(request,'reg.html',{'myform':myform})

def dash(request):
    return render(request,'dash.html')