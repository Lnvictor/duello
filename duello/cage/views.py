from distutils.util import strtobool
from urllib.robotparser import RequestRate
from rest_framework import viewsets
from rest_framework.decorators import action, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from duello.cage.facade import cage_service, question_service, answer_service
from duello.custom_auth.facade import JwtAuthentication


@authentication_classes([JwtAuthentication])
@permission_classes([IsAuthenticated])
class CageViewSet(viewsets.ViewSet):
    def create(self, request):
        return Response(cage_service.create(request.data))

    def update(self, request, id):
        data = request.data
        return Response(cage_service.update(id, data))

    def list(self, request):
        return Response(cage_service.list())

    def retrieve(self, request, id):
        return Response(cage_service.retrieve_by_id(id))
    
    @action(detail=True, methods=['get'])
    def filter(self, request, id):
        creator = strtobool(request.GET.get('creator'))
        participant = strtobool(request.GET.get('participant'))
        filters = {}

        if creator:
            filters.update({'creator_id': id})
        
        if participant:
            filters.update({'participants__id': id})
        
        return Response(cage_service.filter_cages(filters))

    def destroy(self, request, id):
        cage_service.delete(id)
        return Response(status=200)


@authentication_classes([JwtAuthentication])
@permission_classes([IsAuthenticated])
class QuestionViewSet(viewsets.ViewSet):
    def create(self, request):
        return Response(question_service.create(request.data))

    def list(self, request):
        return Response(question_service.list())

    def retrieve(self, request, id):
        return Response(question_service.retrieve_by_id(id))

    def update(self, request, id):
        question_data = request.data
        return Response(question_service.update(id, question_data))
    
    def destroy(self, request, id):
        question_service.delete(id)
        return Response(status=200)


@authentication_classes([JwtAuthentication])
@permission_classes([IsAuthenticated])
class AnswerViewSet(viewsets.ViewSet):
    def create(self, request):
        return Response(answer_service.create(request.data))

    def update(self, request, id):
        data = request.data
        return Response(answer_service.update(id, data))

    def list(self, request):
        return Response(answer_service.list())

    def retrieve(self, request, id):
        return Response(answer_service.retrieve_by_id(id))

    def destroy(self, request, id):
        answer_service.delete(id)
        return Response(status=200)
