from rest_framework.serializers import ModelSerializer
from duello.cage.models import Cage


class CageSerializer(ModelSerializer):
    class Meta:
        model = Cage
        fields = '__all__'
