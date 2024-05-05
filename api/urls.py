from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from . import views

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', views.registerUserView, name='register'),
    path('todo/', views.todoView.as_view(), name='todo'),
    path('make-done/', views.makeTodoDone, name='make-done'),
]
