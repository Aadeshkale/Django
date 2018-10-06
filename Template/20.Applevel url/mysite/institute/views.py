from django.shortcuts import render

# Create your views here.
def pysoft(request):
    return render(request,'institute/pysoft.html')
def djsoft(request):
    return render(request,'institute/djangosoft.html')
     