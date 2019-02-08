from django.shortcuts import render
from info.models import Reg
from info.forms import RegForm
from django.http import HttpResponse 
def index(request):
    if request.method=='POST':
        myform=RegForm(request.POST)
        if myform.is_valid():
            name=request.POST.get('Name','')
            email=request.POST.get('Email','')
            age=request.POST.get('Age','')
            address=request.POST.get('Address','')
            Reg.obj.create(
                name=name,
                email=email,
                age=age,
                address=address,
            )

            return HttpResponse('Data inserted  Successfully :)')
        else:
            return HttpResponse('Data is inserted :(')   
    else:
        myform=RegForm()
        return render(request,'index.html',{'myform':myform})