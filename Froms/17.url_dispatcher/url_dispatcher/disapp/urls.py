from django.conf.urls import url
from django.urls import path
from disapp.views import index,display
urlpatterns=[
    path('',index),
    path('/<str:name>/<int:id>',display),
]