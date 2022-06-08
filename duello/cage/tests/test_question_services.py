import pytest

from duello.cage.facade import question_service


def test_should_create_question(mocker, question_mock):
    mocker.patch('duello.cage.facade.Question.objects', return_value=question_mock)
    mocker.patch('duello.cage.facade.QuestionSerializer.save', return_value=True)
    
    data = {
        'id': question_mock.id,
        'title': question_mock.title,
        'description': question_mock.description,
        'creator': question_mock.creator,
        'cages': question_mock.cages
    }
    assert question_service.create(data)


def test_should_retrieve_all_questions(mocker, question_mock):
    mocker.patch('duello.cage.facade.Question.objects.all', return_value=[question_mock])

    questions = question_service.list()

    assert questions[0].get('title') == question_mock.title


def test_should_retrieve_question_by_id(mocker, question_mock):
    mocker.patch('duello.cage.facade.get_object_or_404', return_value=question_mock)

    question = question_service.retrieve_by_id(question_mock.id)

    assert question.get('title') == question_mock.title


def test_should_update_question(mocker, question_mock):
    mocker.patch("duello.cage.facade.get_object_or_404", return_value=question_mock)
    updated_mock = question_mock
    updated_mock.title = "title 2"
    mocker.patch("duello.cage.facade.QuestionSerializer.update", return_value=updated_mock)

    question_received = question_service.update(question_mock.id, {"title": updated_mock.title})

    assert question_received.get("title") == updated_mock.title


def test_should_delete_question(mocker, question_mock):
    mocker.patch("duello.cage.facade.get_object_or_404", return_value=question_mock)
    mocker.patch("duello.cage.facade.BaseModelService.delete", return_value=question_mock)

    question = question_service.delete(question_mock.id)

    assert question.id == question_mock.id
