from django.conf.urls import url
from movies import views
urlpatterns = [
    url(r'bollywood/',views.bollywood),
    url(r'tollywood/',views.tollywood),
]

