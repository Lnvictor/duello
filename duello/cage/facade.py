from django.shortcuts import get_object_or_404

from duello.cage.models import Cage
from duello.cage.serializers.cage_serializer import CageSerializer
from duello.custom_auth.models import Users


def create_cage(creator, title, description):
    data = {"creator": creator, "title": title, "description": description}
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


def update_cage(id, data):
    obj = get_object_or_404(Cage, pk=id)
    serializer = CageSerializer(data=data)
    serializer.is_valid()
    serializer.update(obj, data)
    return serializer.data


def delete_cage(id):
    cage = get_object_or_404(Cage, pk=id)
    cage.delete()
    return cage
