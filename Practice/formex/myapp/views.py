from django.shortcuts import render
from myapp.form import Myform

def index(request):
    myform=Myform()
    return render(request,'index.html',{'myform':myform})
