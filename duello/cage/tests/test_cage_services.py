import pytest
from duello.cage.facade import create_cage
from django.core.exceptions import ObjectDoesNotExist


def test_should_not_create_cage_due_to_invalid_creator(mocker, user_mock, cage_mock):
    # TODO: Test exception that must be raised when a invalid user_id is sended (Use pytest.raises)
    with pytest.raises(ObjectDoesNotExist):
        mocker.patch('duello.cage.facade.Users.objects', return_value=user_mock)
        mocker.patch('duello.cage.facade.Cage', return_value=cage_mock, side_effect=ObjectDoesNotExist())
        create_cage(user_id=user_mock.id, title=cage_mock.title, description=cage_mock.description)


def test_shoud_create_cage(mocker, user_mock, cage_mock):
    # TODO: Test happy path
    mocker.patch('duello.cage.facade.Users.objects', return_value=user_mock)
    mocker.patch('duello.cage.facade.Cage', return_value=cage_mock)
    assert create_cage(user_id=user_mock.id, title=cage_mock.title, description=cage_mock.description)
