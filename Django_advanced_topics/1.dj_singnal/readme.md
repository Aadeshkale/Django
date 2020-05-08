# Django Signals Example

Django Signals :- 
Are used to implement the signal send and recieve funtionality on certain event i.e Notification System

Signals modules:-
---------------

Signal on models :-

from django.db.models.signals import post_save,pre_save,post_delete

Signal on request

from django.core.signals import request_started,request_finished

Signal on view i.e custom signal
 
from django.core.signals import Signal
mysignal = Signal(providing_args=['info'])



Signals connect:-
---------------
Signal.connect() :- this method is used for to connect specific signal to target receiver
i.e signal handler

example,
    1. post_save.connect(sender=Author,receiver=post_singnal_handler)
    2. 

