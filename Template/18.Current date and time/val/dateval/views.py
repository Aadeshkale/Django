from django.shortcuts import render
from django.template.loader import get_template        # to load templates
from django.http import HttpResponse
import datetime as dt

def index(request):
    op=dt.datetime.now()
    t=get_template('index.html')
    c={'date1':op}
    res=t.render(c)
    return HttpResponse(res)

     