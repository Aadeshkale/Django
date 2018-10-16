from django.shortcuts import render
from multifapp.forms import RegForm
from multifapp.models import Reg
from django.http import HttpResponse
def index(request):
    if request.method=='POST':
        myform=RegForm(request.POST)
        if myform.is_valid():
            name=request.POST.get('name','')
            email=request.POST.get('email','')
            mobile=request.POST.get('mobile','')
            address=request.POST.get('address','')
            myform.save()
            gender=request.POST.get('gender','')
            country=request.POST.get('country','')
            Reg.obj.create(
                name=name,
                email=email,
                mobile=mobile,
                address=address,
                gender=gender,
                country=country,
            )
            
            return HttpResponse('data inserted')
        else:
            return HttpResponse('data not inserted')
    
    else:
        myform=RegForm()
        return render(request,'index.html',{'myform':myform})