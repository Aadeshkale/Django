from django.conf.urls import url
from calapp import views
urlpatterns = [
    url(r'^$',views.index),
    url(r'^add/$',views.add),
    url(r'add/op',views.addop),
    url(r'^sub',views.sub),
    url(r'^mul',views.mul),
    url(r'^div',views.div),
    url(r'^subapp/',views.subop),
    url(r'^mulop/',views.mulop),
    url(r'^divop/',views.divop),
]
