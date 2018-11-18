from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def cources(request):
    return  render(request,'cources.html')    

def computer(request):
    return  render(request,'computer.html')        

def electrical(request):
    return  render(request,'electrical.html')        

def mechnical(request):
    return  render(request,'mechnical.html')        