from django.shortcuts import render,redirect
from calapp.forms import CalForm
from django.http import HttpResponse
def index(request):
   if request.method=="POST":
          return redirect(op)
   else:
        myform=CalForm()
        return render(request,'index.html',{'myform':myform})   

def op(request):
       num1=int(request.POST.get('no1'))
       num2=int(request.POST.get('no2'))
       ops=request.POST.get('ops')
       if  ops=='add':
            sum=num1+num2
            s="Addition is:%s"%(sum)
            return HttpResponse(s) 
       elif ops=="sub":      
            sum=num1-num2
            s="Substraction is:%s"%(sum)
            return HttpResponse(s) 
       elif ops=="mul":      
            sum=num1*num2
            s="Multiplication is:%s"%(sum)
            return HttpResponse(s) 
       elif ops=="div":      
            sum=num1/num2
            s="Division is:%s"%(sum)
            return HttpResponse(s) 
             
             