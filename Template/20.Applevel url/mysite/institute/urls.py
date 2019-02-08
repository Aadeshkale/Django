from django.conf.urls import url
from institute import views

urlpatterns = [
    url(r'pysoft/',views.pysoft),
    url(r'djsoft/',views.djsoft),
]
