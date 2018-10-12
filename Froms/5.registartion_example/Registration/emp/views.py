from django.shortcuts import render
from .forms import EmpForm
from django.http import HttpResponse 
def emp(request):
    if request.method=="POST":
        myform=EmpForm(request.POST)
        if myform.is_valid():
            return HttpResponse('Data inserted Sucessfully')
        else:
            return HttpResponse('Data is not Inserted')


    else:
        myform=EmpForm()
        return render(request,'emp.html',{'myform':myform})
