from django.urls import path
from . import views


urlpatterns = [
    path("register",  views.registerView, name="register"),
    path("login",  views.loginView, name="login"),
    path("logout",  views.logoutView, name="logout"),
    path("delete", views.deleteTodoView, name="delete_todo"),
    path("done", views.markTodoDoneView, name="done"),
    path("todolog", views.todoLogView, name="todolog"),
    path("", views.homeView, name="home"),
]
