from django.shortcuts import render
from .forms import EmpForm
from django.http import HttpResponse
from .models import Emp 
def emp(request):
    if request.method=="POST":
        myform=EmpForm(request.POST)
        if myform.is_valid():
            name=request.POST.get('name','')
            email=request.POST.get('email','')
            salary=request.POST.get('sal','')
            company=request.POST.get('company','')
            location=request.POST.get('location','')
            Emp.objects.create(
                name=name,
                email=email,
                sal=salary,
                company=company,
                location=location,
            )
            return HttpResponse('Data inserted Sucessfully')
        else:
            return HttpResponse('Data is not Inserted')


    else:
        myform=EmpForm()
        return render(request,'emp.html',{'myform':myform})
