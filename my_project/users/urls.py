# users/urls.py
from django.urls import path
from . import views
from .views import UserListView

urlpatterns = [
    path('', views.home, name="home"),
    path("signup/", views.SignUp.as_view(), name="signup"),
    path('search', UserListView.as_view(), name='search')
]
