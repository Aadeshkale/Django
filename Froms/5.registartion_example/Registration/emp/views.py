from django.shortcuts import render
from .forms import EmpForm 
def emp(request):
    if request.method=="POST":
        pass
    else:
        myform=EmpForm()
        return render(request,'emp.html',{'myform':myform})
