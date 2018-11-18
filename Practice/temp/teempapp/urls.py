from django.conf.urls import url
from teempapp import views
urlpatterns=[
    url(r'^$',views.index),
]