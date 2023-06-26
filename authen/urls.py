from django.urls import path, include
from .views import HomeView, LoginView, LogoutView, LogoutView, RegisterView


urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("", HomeView.as_view(), name="home"),
]
