from django.conf.urls import url
from . import views
urlpatterns = [
    url('^$',views.div),
    url('div',views.op),
]
