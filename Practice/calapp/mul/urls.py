from django.conf.urls import url
from mul import views
urlpatterns = [
    url(r'^$',views.mul),
    url(r'op/',views.op),
]