from django.shortcuts import render
from disapp.models import Info
from django.http import HttpResponse
def index(request):
    data=Info.objects.all()
    for i in data:
        print(i)
    return render(request,'index.html',{'data':data})

def display(request,name,id):
    data=Info.objects.get(id=id)
    return render(request,'display.html',{'data':data})
    