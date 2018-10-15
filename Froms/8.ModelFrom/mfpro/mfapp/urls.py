from django.conf.urls import url
from mfapp import views
urlpatterns = [
    url(r'^$',views.index)
]
