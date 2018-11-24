from django.conf.urls import url
from myapp.views import *
urlpatterns = [
    url(r'^$',index),
    url(r'^insert',insert),
    url(r'^display',display),
    url(r'^update',update),
    url(r'^delete',delete),
]
