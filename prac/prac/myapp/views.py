from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse 
from myapp.models import Emp
# Create your views here.

def index(request):
    response=HttpResponse()
    response.write("<html><body>\n")
    response.write("<h1>Employee Details:</h1>")
    response.write("<hr>")
    emp_list=Emp.objects.all()
    for e in emp_list:
        response.write("<li><a href='/myapp/info/%d/'>%s</a></li>"%(e.id,e.name))
    response.write("</body></html>")

    




    return HttpResponse(response)