from django.shortcuts import render
from myapp.forms import Employee
from django.http import HttpResponse
def index(request):
    if request.method == 'POST':
        myform=Employee(request.POST)
        if myform.is_valid():
            return HttpResponse('data is valid')
        else:
            return HttpResponse('data is not vaild')    

    else:
        myform = Employee()
        return render(request,'index.html',{'myform':myform})    