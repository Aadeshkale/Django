from django.conf.urls import url 
from .import views
urlpatterns = [
    url(r'^$',views.add),
    url(r'add/',views.op)
]
