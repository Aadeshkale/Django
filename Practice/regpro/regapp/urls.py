from django.urls import re_path,include
from regapp.views import IndexView,RegisterView,LoginView,CompleteView,ApanelView
urlpatterns = [
    re_path(r'^$',IndexView.as_view()),
    re_path(r'login',LoginView.as_view()),
    re_path(r'register',RegisterView.as_view()),
    re_path(r'^register/complete$',CompleteView.as_view()),
]
