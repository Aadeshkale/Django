from django.conf.urls import url
from add import views
urlpatterns = [
    url(r'^$',views.add),
    url(r'op/',views.op),
]
