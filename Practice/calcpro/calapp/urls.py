from django.conf.urls import url
from calapp.views import *
urlpatterns = [
    url(r'^$',index),
    url(r'op',op),
]
 