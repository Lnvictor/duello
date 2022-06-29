from django.db.models import Model
from django.shortcuts import get_object_or_404
from rest_framework.serializers import ModelSerializer

from duello.cage.models import Cage, Question, Answer
from duello.cage.serializers import CageSerializer, QuestionSerializer, AnswerSerializer
from duello.custom_auth.models import Users


class BaseModelService:
    model_type = Model
    serializer_type = ModelSerializer

    def __init__(self):
        self._serializer = self.serializer_type()

    def _renew_serializer(self, instance=None, data=None):
        if self._serializer:
            del(self._serializer)

        if instance is not None:
            self._serializer = self.serializer_type(instance=instance)
            return
        
        if data is not None:
            self._serializer = self.serializer_type(data=data)
            return

        raise Exception('You must pass either data or instance fields')


    def create(self, data):
        self._renew_serializer(data=data)
        self._serializer.is_valid()
        cage = self._serializer.save()
        return self._serializer.data
    
    
    def retrieve_by_id(self, id):
        obj = get_object_or_404(self.model_type, pk=id)
        self._renew_serializer(instance=obj)
        return self._serializer.data
    
    def list(self):
        obj_list = []
        for obj in self.model_type.objects.all():
            self._renew_serializer(instance=obj)
            obj_list.append(self._serializer.data)

        return obj_list
    
    def update(self, id, data):
        obj = get_object_or_404(self.model_type, pk=id)
        self._renew_serializer(data=data) 
        self._serializer.is_valid()
        self._serializer.update(obj, data)
        return self._serializer.data
    
    
    def delete(self, id):
        obj = get_object_or_404(self.model_type, pk=id)
        obj.delete()
        obj.save()
        return obj


class CageService(BaseModelService):
    model_type = Cage
    serializer_type = CageSerializer

    def filter_cages(self, filters):
        cages_response = {}

        for pair in filters.items():
            tmp_filter = {pair[0]: pair[1]}
            cages = self.model_type.objects.filter(**tmp_filter)
            cages_response[pair[0]] = []

            for cage in cages:
                self._renew_serializer(instance=cage)
                cages_response[pair[0]].append(self._serializer.data)

        return cages_response

class QuestionService(BaseModelService):
    model_type = Question
    serializer_type = QuestionSerializer


class AnswerService(BaseModelService):
    model_type = Answer
    serializer_type = AnswerSerializer

# Singleton
cage_service = CageService()
question_service = QuestionService()
answer_service = AnswerService()
