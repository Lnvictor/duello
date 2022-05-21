from duello.custom_auth.models import Users
from duello.cage.serializers.cage_serializer import CageSerializer


def create_cage(creator, title, description):
    data = {'creator': creator, 'title': title, 'description': description}
    serializer = CageSerializer(data=data)
    serializer.is_valid()
    serializer.save()
    return serializer.data

