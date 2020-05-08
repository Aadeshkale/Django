from django.shortcuts import render
from django.views import View
from django.http.response import HttpResponse
from django.core.signals import request_finished
from django.dispatch import receiver
from django.core.signals import Signal


mysignal = Signal(providing_args=['info'])

class IndexView(View):

    def get(self,request):
        mysignal.send(sender=self.__class__,info="index_view")
        return HttpResponse("This is home page to show signal's demo ")

def index(request):
    return HttpResponse("This is home page to show signal's demo ")




def handler_request_finish(sender,**kwargs):
    print("the home page is visited ")

mysignal.connect(receiver=handler_request_finish)

