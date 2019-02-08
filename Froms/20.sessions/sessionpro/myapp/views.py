from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib import sessions
from django.contrib.auth import authenticate
from myapp.forms import LoginForm
from django.contrib import messages 
class LoginView(View):
    def get(self,request):  
        myform=LoginForm()
        return render(request,'login.html',{'myform':myform})
    def post(self,request):
        myfrom=LoginForm(request.POST)
        if myfrom.is_valid():
            username=request.POST['username']
            password=request.POST['password']
            if authenticate(request,username=username,password=password):
                request.session[username]=username
                return redirect('home',username)
            else:
                return HttpResponse(self,'Invalid User :(')
class HomeView(View):
    def get(self,request,username):
        if request.session.has_key(username):
            return render(request,'home.html')
        else:
            return HttpResponse('You need to login first')
class LogoutView(View):
    def get(self,request,username):
        del request.session[username]
        return redirect('login')
