from django.shortcuts import render
from empapp.forms import EmpForm

# Create your views here.
def empview(request):
    myform=EmpForm()
    return render(request,'emp.html',{'myform':myform})