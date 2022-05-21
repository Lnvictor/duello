from duello.custom_auth.models import Users
from duello.cage.models import Cage
from duello.cage.serializers.cage_serializer import CageSerializer
from django.shortcuts import  get_object_or_404


def create_cage(creator, title, description):
    data = {'creator': creator, 'title': title, 'description': description}
    serializer = CageSerializer(data=data)
    serializer.is_valid()
    serializer.save()
    return serializer.data


def retrieve_cage_by_id(id):
   cage = get_object_or_404(Cage, pk=id)
   serializer = CageSerializer(cage)
   return serializer.data


def list_cages():
    queryset = CageSerializer(Cage.objects.all(), many=True)
    return queryset.data

