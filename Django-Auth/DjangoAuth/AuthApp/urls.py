from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage, name="home-page"),
    path('/login', views.UserLogin, name="login-page"),
    path('/logout', views.UserLogout, name="logout-page"),
    path('/register', views.UserRegister, name="register-page"),
]
