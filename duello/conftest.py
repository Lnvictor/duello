from pytest import fixture
import os
from unittest.mock import MagicMock

import django


# needs django.setup() to import some modules
django.setup()

from duello.custom_auth.facade import JwtHandler
from duello.custom_auth.models import Users
from duello.cage.models import Cage


@fixture
def jwt_handler_with_invalid_certificate():
    os.environ["JWT_PUBLIC_KEY"] = "PUBLIC_KEY"
    os.environ['JWT_PRIVATE_KEY'] = "PRIVATE_KEY"
    jwt_handler = JwtHandler()

    return jwt_handler


@fixture
def jwt_handler():
    os.environ["JWT_PUBLIC_KEY"] = open('keys_rsa.pub', 'r').read()
    os.environ["JWT_PRIVATE_KEY"] = open('keys_rsa', 'r').read()

    jwt_handler = JwtHandler()
    return jwt_handler


@fixture
def user_mock(mocker):
    # User model mock
    user_mock = Users(id=1, user_name='Lnvictor', user_email='vh141299@gmail.com', user_last_name='Pereira')
    return MagicMock(return_value=user_mock)


@fixture
def cage_mock(mocker, user_mock):
    # Cage model Mock
    cage_mock = Cage(title='Champions cage', creator=user_mock.return_value, description='This is a cage for champions. Weaks are not allowed')
    return MagicMock(return_value=cage_mock)

