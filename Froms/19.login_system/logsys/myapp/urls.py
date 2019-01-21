from django.urls import path,re_path
from django.conf.urls import url
from myapp.views import *
from django.contrib.auth import views
urlpatterns = [
    path('',index),
    re_path(r'register',register),
    re_path(r'dash',dash),
    re_path(r'login',views.LoginView.as_view(template_name="login.html"),name="my_login"),
]
