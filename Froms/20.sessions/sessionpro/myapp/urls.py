from django.urls import re_path
from myapp.views import LoginView,HomeView,LogoutView
urlpatterns = [
    re_path(r'^$',LoginView.as_view(),name='login'),
    re_path(r'^/home/(?P<username>\w+)/$',HomeView.as_view(),name='home'),
    re_path(r'^/home/(?P<username>\w+)/logout/$',LogoutView.as_view(),name='logout'),         
]
