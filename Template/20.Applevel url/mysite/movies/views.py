from django.shortcuts import render

# Create your views here.
def bollywood(request):
   return  render(request,'movies/bollywood.html') 

def tollywood(request):
    return render(request,'movies/tollywood.html')   