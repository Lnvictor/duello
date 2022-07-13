import pytest
from django.core.exceptions import ObjectDoesNotExist

from duello.cage.facade import cage_service


def test_should_not_create_cage_due_to_invalid_creator(mocker, user_mock, cage_mock):
    with pytest.raises(ObjectDoesNotExist):
        mocker.patch("duello.cage.facade.Users.objects", return_value=user_mock)
        mocker.patch(
            "duello.cage.facade.CageSerializer.save",
            return_value=cage_mock,
            side_effect=ObjectDoesNotExist(),
        )
        data = {'creator': user_mock.id, 'title': cage_mock.title, 'description': cage_mock.description}
        cage_service.create(data)


def test_shoud_create_cage(mocker, user_mock, cage_mock):
    mocker.patch("duello.cage.facade.Users.objects", return_value=user_mock)
    mocker.patch("duello.cage.facade.CageSerializer.save", return_value=True)
    mocker.patch("duello.cage.facade.Cage", return_value=cage_mock)
    data = {'creator': user_mock.id, 'title': cage_mock.title, 'description': cage_mock.description}
    assert cage_service.create(data)


def test_should_retrieve_all_cages(mocker, cage_mock):
    mocker.patch(
        "duello.cage.facade.Cage.objects.all", return_value=[cage_mock, cage_mock]
    )
    cages = cage_service.list()
    assert cages[0].get("title") == cage_mock.title


@pytest.mark.parametrize('filter_type', ['creator', 'participant'])
def test_should_retrieve_cages_by_creator_id(filter_type, mocker, cage_mock, user_mock):
    filter_mapping = {'creator': 'creator_id', 'participant': 'participants__id'}
    mocker.patch('duello.cage.facade.Cage.objects.filter', return_value=[cage_mock])
    filters = {
        filter_mapping[filter_type]: user_mock.id
    }

    data = cage_service.filter_by(filters=filters)

    assert data.get(filter_mapping[filter_type])[0].get('title') == cage_mock.title


def test_should_retrieve_cage_by_id(mocker, cage_mock):
    mocker.patch("duello.cage.facade.get_object_or_404", return_value=cage_mock)
    cage = cage_service.retrieve_by_id(cage_mock.id)

    assert cage.get("title") == cage_mock.title


def test_should_update_cage(mocker, cage_mock):
    mocker.patch("duello.cage.facade.get_object_or_404", return_value=cage_mock)
    updated_mock = cage_mock
    updated_mock.title = "title 2"
    mocker.patch("duello.cage.facade.CageSerializer.update", return_value=updated_mock)

    cage_received = cage_service.update(cage_mock.id, {"title": updated_mock.title})

    assert cage_received.get("title") == updated_mock.title


def test_should_delete_cage(mocker, cage_mock):
    mocker.patch("duello.cage.facade.get_object_or_404", return_value=cage_mock)
    mocker.patch("duello.cage.facade.BaseModelService.delete", return_value=cage_mock)

    cage = cage_service.delete(cage_mock.id)

    assert cage.id == cage_mock.id
