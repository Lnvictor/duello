import pytest
from django.core.exceptions import ObjectDoesNotExist

from duello.cage.facade import create_cage, list_cages, retrieve_cage_by_id, update_cage, delete_cage


def test_should_not_create_cage_due_to_invalid_creator(mocker, user_mock, cage_mock):
    with pytest.raises(ObjectDoesNotExist):
        mocker.patch("duello.cage.facade.Users.objects", return_value=user_mock)
        mocker.patch(
            "duello.cage.facade.CageSerializer",
            return_value=cage_mock,
            side_effect=ObjectDoesNotExist(),
        )
        mocker.patch('duello.cage.facade.CageSerializer.save', return_value=True)
        create_cage(
            creator=user_mock,
            title=cage_mock.title,
            description=cage_mock.description,
        )


def test_shoud_create_cage(mocker, user_mock, cage_mock):
    mocker.patch("duello.cage.facade.Users.objects", return_value=user_mock)
    mocker.patch('duello.cage.facade.CageSerializer.save', return_value=True)
    mocker.patch("duello.cage.facade.Cage", return_value=cage_mock)
    assert create_cage(
        creator=user_mock, title=cage_mock.title, description=cage_mock.description
    )


def test_should_retrieve_all_cages(mocker, cage_mock):
    mocker.patch('duello.cage.facade.Cage.objects.all', return_value=[cage_mock, cage_mock])
    cages = list_cages()
    assert cages[0].get('title') == cage_mock.title


def test_should_retrieve_cage_by_id(mocker, cage_mock):
    mocker.patch('duello.cage.facade.get_object_or_404', return_value=cage_mock)
    cage = retrieve_cage_by_id(cage_mock.id)

    assert cage.get('title') == cage_mock.title

