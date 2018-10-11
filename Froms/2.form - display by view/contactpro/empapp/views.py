from django.shortcuts import render

# Create your views here.
def empview(request):
    return render(request,'emp.html')