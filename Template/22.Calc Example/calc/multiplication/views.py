from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template,Context
from django.template.loader import get_template
def mul(request):
    return render (request,'mul/mul.html')

def op(request):
    x=int(request.GET['val1'])
    y=int(request.GET['val2'])
    z=x*y
    t=get_template('mul/mul.html')
    c={'result':z}
    page=t.render(c)
    return HttpResponse(page)