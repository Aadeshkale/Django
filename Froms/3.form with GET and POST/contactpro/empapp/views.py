from django.shortcuts import render
from . forms import EmpForm
from django.http import HttpResponse
# Create your views here.
def emp(request):
    if request.method=='POST':
        myform=EmpForm(request.POST)
        if myform.is_valid():
            return HttpResponse("Data is valid :)")
        else:
            return HttpResponse("Data is not valid :(")
    
    else:
        myform=EmpForm()
        return render(request,'emp.html',{'myform':myform})
