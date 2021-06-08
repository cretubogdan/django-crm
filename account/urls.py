from django.contrib.auth import logout
from django.urls import path
from .views import login_view, logout_view, register_view

urlpatterns = [
    path('login/', login_view, name='login-view'),
    path('logout/', logout_view, name='logout-view'),
    path('register/', register_view, name='register-view'),
]
