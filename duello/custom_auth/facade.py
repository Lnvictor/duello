import jwt
from cryptography.hazmat.primitives import serialization
from decouple import config
from rest_framework.authentication import BaseAuthentication


class JwtHandler:
    def __init__(self) -> None:
        self.__key = serialization.load_ssh_private_key(
            config("JWT_PRIVATE_KEY").encode(), password=b""
        )
        self.__pkey = serialization.load_ssh_public_key(
            config("JWT_PUBLIC_KEY").encode()
        )

    def gen_token(self, *args, **kwargs):
        data = dict(**kwargs)
        return jwt.encode(data, self.__key, algorithm="RS256")

    def decode_token(self, token):
        return jwt.decode(token, self.__key, algorithms=["RS256"])


class JwtAuthentication(BaseAuthentication):
    def __init__(self):
        super().__init__()
        self.handler = JwtHandler()

    def authenticate(self, request):
        header = self.authenticate_header(request)

        if not header or not "Bearer" in header:
            return None

        return self.get_credentials(header.split()[1])

    def authenticate_header(self, request):
        try:
            return request.headers["Authorization"]
        except KeyError:
            return None

    def get_credentials(self, token):
        payload = self.handler.decode_token(token)
        return payload
