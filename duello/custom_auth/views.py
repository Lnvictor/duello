from this import d
from django.shortcuts import get_object_or_404
from rest_framework.decorators import permission_classes, api_view, authentication_classes
from rest_framework.viewsets import ViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from .serializers import UserSerializer
from .facade import JwtAuthentication, JwtHandler
from .models import Users


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
        return Response({"message": "Invalid credentials"}, status=403)

    resp = {
        "name": user.user_name,
        "last_name": user.user_last_name,
        "email": user.user_email,
        "token": JwtHandler().gen_token(email=user.user_email, name=user.user_name, last_name=user.user_last_name)
    }

    return Response(resp)
