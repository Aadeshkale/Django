from django.conf.urls import url
from proapp import views
urlpatterns = [
    url(r'^$',views.index),
    url(r'^$',views.insert),
]
