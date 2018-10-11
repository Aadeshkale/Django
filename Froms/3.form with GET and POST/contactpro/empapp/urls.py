from django.conf.urls import url
from empapp import views 
urlpatterns = [
    url(r'^$',views.emp),
]
