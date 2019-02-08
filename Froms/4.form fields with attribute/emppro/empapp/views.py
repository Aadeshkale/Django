from django.shortcuts import render
from empapp.forms import EmpFrom
# Create your views here.
def emp(request):
    if request.method == "POST":
        pass
    else:
        myform=EmpFrom()
        return render(request,'emp.html',{'myform':myform})
