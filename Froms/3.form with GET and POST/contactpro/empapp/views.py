from django.shortcuts import render
from . forms import EmpForm
# Create your views here.
def emp(request):
    myform=EmpForm()
    return render(request,'emp.html',{'myform':myform})