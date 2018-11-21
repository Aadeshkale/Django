from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def add(request):
    response=render(request,'index.html')
    response.set_cookie('color','red')
    return response

def remove(request):
    response=render(request,'index.html')
    response.delete_cookie('color')
    return response

def count(request):
    response=render(request,'index.html')
    if request.COOKIES.get('visit'):
        cnt=int(request.COOKIES.get('visit'))
        cnt+=1
        response.set_cookie("visit",str(cnt))
        return response
    else:
        response.set_cookie('visit','1')    
        return response