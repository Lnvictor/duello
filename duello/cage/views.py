from rest_framework import viewsets
from rest_framework.decorators import (authentication_classes,
                                       permission_classes)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from duello.cage.facade import cage_service, question_service
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

    def destroy(self, request, id):
        cage_service.delete(id)
        return Response(status=200)


class QuestionViewSet(viewsets.ViewSet):
    #TODO: IMPLEMENTAR VIEWSET PARA QUESTOES
    pass
