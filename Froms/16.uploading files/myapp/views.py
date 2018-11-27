from django.shortcuts import render
from myapp.forms import FileForm
from myapp.models import File
from django.http import HttpResponse
def index(request):
    if request.method=="POST":
        myform=FileForm(request.POST,request.FILES)
        if myform.is_valid():
            myform.save()
            return HttpResponse('File Uploaded Successfully')
        else:
            return HttpResponse('File Uploaded Successfully')    
    else:
        myform=FileForm()
        return render(request,'index.html',{'myform':myform})