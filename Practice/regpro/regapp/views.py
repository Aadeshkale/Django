from django.shortcuts import render
from django.views import View

class IndexView(View):
    def get(self,request):
        return render(request,'index.html')

class RegisterView(View):
    def get(self,request):
        return render(request,'registration/registration_form.html')        

class LoginView(View):
    def get(self,request):
        return render(request,'registration/login.html')     
 
class CompleteView(View):
    def get(self,request):
        return render(request,'registration/registration_complete.html')

class ApanelView(View):
    def get(self,request):
        return render(request,'apanel.html')
