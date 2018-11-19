from django.conf.urls import url
from sub import views
urlpatterns = [
    url(r'^$',views.sub),
    url(r'op',views.op),
]
