from django.db.models import Model
from django.shortcuts import get_object_or_404
from rest_framework.serializers import ModelSerializer

from duello.cage.models import Cage, Question
from duello.cage.serializers.cage_serializer import CageSerializer, QuestionSerializer
from duello.custom_auth.models import Users


class BaseModelService:
    model_type = Model
    serializer_type = ModelSerializer

    def __init__(self):
        self._serializer = self.serializer_type()
        self._list_serializer = self.serializer_type(many=True)

    def create(self, data):
        if self._serializer is not None:
            del(self._serializer)

        self._serializer = self.serializer_type(data=data)
        self._serializer.is_valid()
        cage = self._serializer.save()
        return self._serializer.data
    
    
    def retrieve_by_id(self, id):
        obj = get_object_or_404(self.model_type, pk=id)
        self._serializer.instance = obj
        return self._serializer.data
    
    def list(self):
        self._list_serializer.instance = self.model_type.objects.all()
        return self._list_serializer.data
    
    
    def update(self, id, data):
        obj = get_object_or_404(Cage, pk=id)
        if self._serializer is not None:
            del(self._serializer)
        self._serializer = self.serializer_type(data=data)
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


class QuestionService(BaseModelService):
    model_type = Question
    serializer_type = QuestionSerializer


# Singleton
cage_service = CageService()
question_service = QuestionService()
