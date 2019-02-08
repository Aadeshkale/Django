from django.shortcuts import render
from django.template import Template,Context
from django.template.loader import get_template
from django.http import HttpResponse
def div(request):
    return render(request,'div/divi.html')

def op(request):
    x=int(request.GET['val1'])
    y=int(request.GET['val2'])
    z=x//y
    t=get_template('div/divi.html')
    c={'result':z}
    page=t.render(c)
    return HttpResponse(page)
