from django.shortcuts import render
from mfapp.forms import StuForm
from django.http import HttpResponse
def index(request):
    if request.method=='POST':
        myform=StuForm(request.POST)
        if myform.is_valid():
            myform.save()
            return HttpResponse('Data Inserted Successfully :)')
        else:
            return HttpResponse('Data is not Inserted :(')
    else:
        myform=StuForm()
        return render(request,'index.html',{'myform':myform})

