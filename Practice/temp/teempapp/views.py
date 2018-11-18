from django.shortcuts import render
import datetime
# Create your views here.
def index(request):
    date=datetime.datetime.now
    print(date)
    return render(request,'index.html',{'date':date})