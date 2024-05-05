from django.urls import path
from . import views


urlpatterns = [
    path("register",  views.registerView, name="register"),
    path("login",  views.loginView, name="login"),
    path("", views.homeView, name="home"),
]
