from rest_framework import viewsets
from rest_framework.decorators import authentication_classes, permission_classes
from duello.custom_auth.facade import JwtAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from duello.cage.serializers.cage_serializer import CageSerializer


@authentication_classes([JwtAuthentication])
@permission_classes([IsAuthenticated])
class CageViewSet(viewsets.ViewSet):
    def create(self, request):
        serializer = CageSerializer(data=request.data)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data)

    def get_permission(self):
        return [IsAuthenticated()]
