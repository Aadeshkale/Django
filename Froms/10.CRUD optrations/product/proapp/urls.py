from django.conf.urls import url
from proapp import views
urlpatterns = [
    url(r'^$',views.index),
    url(r'insert/',views.insert),
    url(r'display/',views.display),
    url(r'update/',views.update),
    url(r'delete/',views.delete),
]
