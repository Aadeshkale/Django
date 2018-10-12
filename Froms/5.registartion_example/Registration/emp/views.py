from django.shortcuts import render

def emp(request):
    if request.method=="POST":
        pass
    else:
       return render(request,'emp.html')
       