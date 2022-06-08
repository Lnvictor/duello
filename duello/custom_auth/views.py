import secrets
import string
from datetime import datetime, timedelta

from decouple import config
from rest_framework.decorators import (api_view, authentication_classes,
                                       permission_classes)
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from .facade import JwtAuthentication, JwtHandler
from .jobs import MailSchema, send_confirmation_mail
from .models import Users
from .serializers import UserSerializer


@api_view(["POST"])
@authentication_classes([JwtAuthentication])
@permission_classes([AllowAny])
def sign_up(request):
    data = request.data
    serializer = UserSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    data = serializer.data

    return Response(serializer.data)


@api_view(["POST"])
@authentication_classes([JwtAuthentication])
@permission_classes([AllowAny])
def login(request): 
    data = request.data
    user = Users.objects.filter(user_email=data["email"]).first()

    if not user or user.password != data["password"]:
        return Response({"message": "Invalid credentials"}, status=401)

    jwt_token = JwtHandler().gen_token(
        email=user.user_email, name=user.user_name, last_name=user.user_last_name
    )

    if not user.verified:
        return Response({"message": "unverified user", "token": jwt_token}, status=401)

    user.last_login = datetime.now() - timedelta(hours=3)
    user.save()

    resp = {
        "name": user.user_name,
        "last_name": user.user_last_name,
        "email": user.user_email,
        "token": jwt_token,
    }

    return Response(resp)


@api_view(["POST"])
@authentication_classes([JwtAuthentication])
@permission_classes([IsAuthenticated])
def send_mail(request):
    data = request.data
    mail_token = "".join(secrets.choice(string.ascii_letters) for _ in range(6))
    mail_schema = MailSchema(
        subject="Duello Confirmation code",
        body=f"Your code is {mail_token}",
        sender=config("DUELLO_MAIL"),
        destinatary=data["destinatary"],
    )
    user = request.user
    user.last_sended_token = mail_token
    user.save()
    return Response(send_confirmation_mail(mail_schema))


@api_view(["POST"])
@authentication_classes([JwtAuthentication])
@permission_classes([IsAuthenticated])
def verify_mail_code(request):
    data = request.data

    if "code" in data.keys() and data["code"] == request.user.last_sended_token:
        request.user.verified = True
        request.user.save()
        return Response({"message": "User verified"})

    return Response({"message": "Invalid info was provided"}, status=400)
