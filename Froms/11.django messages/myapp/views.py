from django.shortcuts import render
from myapp.forms import RegForm
from django.contrib import messages
from django.http import HttpResponseRedirect
def index(request):
    if request.method=='POST':
        myfrom=RegForm(request.POST)
        if myfrom.is_valid():
            myfrom.save()
            messages.info(request,'Data Added Sucessfully')
            return HttpResponseRedirect(request.path_info)  
        else:
            messages.warning(request,'Data Is Invaild')
            return HttpResponseRedirect(request.path_info)
    else:
        myform=RegForm()
        return render(request,'index.html',{'myform':myform})
        