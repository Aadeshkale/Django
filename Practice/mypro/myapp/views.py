from django.shortcuts import render,redirect
from myapp.forms import RegForm
from myapp.models import Reg
from django.contrib import messages
def index(request):
    if request.method=="POST":
        myform=RegForm(request.POST)
        if myform.is_valid():
            femail=request.POST.get('email')
            if Reg.objects.filter(email=femail):
                messages.info(request,'email is already register')
            else:
                myform.save()
                messages.info(request,'Data stored Successfully')
                
            return redirect(index)        
        else:
            messages.warning(request,'Data is invalid')
            return redirect(index)    
    else:
        myform=RegForm()
        return render(request,'index.html',{'myform':myform})