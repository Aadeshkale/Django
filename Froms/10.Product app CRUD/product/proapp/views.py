from django.shortcuts import render
from django.http import HttpResponse
from proapp.forms import ProductForm
from proapp.models import Product
def index(request):
    return render (request,'index.html')

def insert(request):
    if request.method=='POST':
        myform=ProductForm(request.POST)
        if myform.is_valid():
            myform.save()
            return HttpResponse('Data Inserted Successfully')
        else:
            return HttpResponse('Data Not Inserted')    
    else:
        myform=ProductForm()
        return render (request,'insert.html',{'myform':myform}) 

def display(request):
            data=Product.obj.all()
            return render (request,'display.html',{'data':data}) 
    