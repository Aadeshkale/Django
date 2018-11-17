from django.shortcuts import render
from valapp import form
from django.contrib import messages
def index(request):
    if request.method=="POST":
        valform=form.ValForm(request.POST)
        if valform.is_valid():
            messages.info(request,'Data is valid')
            return render(request,'index.html')
        else:
            messages.info(request,'Data is Invalid')
            return render(request,'index.html')          
    else:
        valform=form.ValForm()
        return render(request,'index.html',{'valform':valform})    