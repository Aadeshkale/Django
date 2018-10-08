from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$',views.home),
    url(r'python',views.python),
    url(r'django',views.django),
    url(r'restapi',views.restapi),
]
