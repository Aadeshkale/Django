from django.conf.urls import url
from cookiesapp.views import *
urlpatterns = [
    url(r'^$',index),
    url(r'add/',add),
]
