from django.conf.urls import url
from myapp.views import *
urlpatterns = [
    url(r'^$',index),
    url(r'^cources/$',cources),
    url(r'^cources/computer',computer),
    url(r'^cources/electrical',electrical),
    url(r'^cources/mechnical',mechnical),
]
