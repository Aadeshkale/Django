from django.conf.urls import url
from addapp import views
urlpatterns=[
    url(r'^$',views.index),
    url(r'/addop',views.add)
]