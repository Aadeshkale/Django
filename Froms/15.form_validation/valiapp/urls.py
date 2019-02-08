from django.conf.urls import url
from valiapp.views import index
urlpatterns = [
    url(r'^$',index),
]
