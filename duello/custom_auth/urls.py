from django.urls import path

from .views import login, sign_up

urlpatterns = [
    path("signup/", sign_up, name="sign_up"),
    path("login", login, name="login"),
]
