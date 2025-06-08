from django.urls import path
from .views import UserLoginView, UserRegister

urlpatterns = [
    path("user_register/", UserRegister.as_view()),
    path("user_login/", UserLoginView.as_view())
]