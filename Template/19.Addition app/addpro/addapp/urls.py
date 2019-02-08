from django.conf.urls import url
from .views import index,addfun
urlpatterns = [
    url(r"^$",index),
    url(r'^add/',addfun),
]

