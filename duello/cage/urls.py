from django.urls import path

from .views import CageViewSet, QuestionViewSet, AnswerViewSet

urlpatterns = [
    path("cage", CageViewSet.as_view({"post": "create", "get": "list"}), name="cage"),
    path(
        "cage/<int:id>",
        CageViewSet.as_view({"get": "retrieve", "delete": "destroy", "put": "update"}),
        name="cage_by_id",
    ),
    path("cage/filter/<int:id>", CageViewSet.as_view({"get": "filter"}), name="filter_cage"),
    path("question", QuestionViewSet.as_view({"post": "create", "get": "list"}), name="question"),
    path(
        "question/<int:id>",
        QuestionViewSet.as_view({"get": "retrieve", "delete": "destroy", "put": "update"}),
        name="question_by_id",
    ),
    path("question/filter/<int:id>", QuestionViewSet.as_view({'get': 'filter'}), name="filter_question"),
    path("answer", AnswerViewSet.as_view({"post": "create", "get": "list"}), name="answer"),
    path(
        "answer/<int:id>",
        AnswerViewSet.as_view({"get": "retrieve", "delete": "destroy", "put": "update"}),
        name="answer_by_id",
    ),
    path("answer/filter/<int:id>", AnswerViewSet.as_view({"get": "filter"}), name="filter_answer")
]
