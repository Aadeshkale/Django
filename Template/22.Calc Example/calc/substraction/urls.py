from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$',views.sub),
    url(r'sub/',views.op),
]
