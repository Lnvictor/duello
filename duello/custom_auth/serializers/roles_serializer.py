from rest_framework.serializers import ModelSerializer
from ..models import Roles


class RolesSerializer(ModelSerializer):
    class Meta:
        model = Roles
        fields = '__all__'