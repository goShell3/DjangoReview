from django.urls import path
# from .views import UserLoginView, UserRegister
from . import views

urlpatterns = [
    path("user_register/", views.UserRegister.as_view()),
    path("user_login/", views.UserLoginView.as_view())
]