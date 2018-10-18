from django.shortcuts import render
from django.http import HttpResponse
from proapp.forms import ProductForm , DeleteForm
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

def update(request):
    if request.method=='POST':
        myform=ProductForm(request.POST)
        if myform.is_valid():
            ids=request.POST.get('productId','')
            name=request.POST.get('productName','')
            cost=request.POST.get('productCost','')
            quantity=request.POST.get('productQuantity','')
            description=request.POST.get('productDescription','')
            if Product.obj.get(productId=ids):
                res=Product.obj.get(productId=ids)
                res.productName=name
                res.productCost=cost
                res.productQuantity=quantity
                res.productDescription=description
                res.save()
                return HttpResponse('Data Updated Successfully')       
            else:
                return HttpResponse('Data Not Updated')    
    else:
        myform=ProductForm()
        return render (request,'update.html',{'myform':myform}) 

def delete(request):
    if request.method=="POST":
        myform=DeleteForm(request.POST)
        ids=request.POST.get('productId','')
        if myform.is_valid():
            if Product.obj.get(productId=ids):
               pro=Product.obj.get(productId=ids)
               pro.delete()
               pro.save() 
               return HttpResponse('Product Deleted Successfully ')
            else:
                return HttpResponse('Product Not Deleted') 
    else:
        myform=DeleteForm()
        return render(request,'delete.html',{'myform':myform})    
