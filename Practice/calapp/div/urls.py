from django.conf.urls import url
from div import views
urlpatterns = [
    url(r'^$',views.div),
    url(r'op',views.op),
]
