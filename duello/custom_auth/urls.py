from django.urls import path

from .views import login, send_mail, sign_up, verify_mail_code

urlpatterns = [
    path("signup", sign_up, name="sign_up"),
    path("login", login, name="login"),
    path("send_confirmation_mail", send_mail, name="send_confirmation_mail"),
    path("verify_code", verify_mail_code, name="verify_code"),
]
