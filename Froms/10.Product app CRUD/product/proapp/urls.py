from django.conf.urls import url
from proapp import views
urlpatterns = [
    url(r'^$',views.index),
    url(r'insert/',views.insert),
    url(r'display/',views.display),
]
