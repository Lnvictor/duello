from rest_framework import viewsets
from rest_framework.decorators import (authentication_classes,
                                       permission_classes)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from duello.cage.facade import (create_cage, delete_cage, list_cages,
                                retrieve_cage_by_id, update_cage)
from duello.cage.serializers.cage_serializer import CageSerializer
from duello.custom_auth.facade import JwtAuthentication


@authentication_classes([JwtAuthentication])
@permission_classes([IsAuthenticated])
class CageViewSet(viewsets.ViewSet):
    def create(self, request):
        return Response(create_cage(**request.data))

    def update(self, request, id):
        data = request.data
        return Response(update_cage(id, data))

    def list(self, request):
        return Response(list_cages())

    def retrieve(self, request, id):
        return Response(retrieve_cage_by_id(id))

    def destroy(self, request, id):
        delete_cage(id)
        return Response(status=200)
