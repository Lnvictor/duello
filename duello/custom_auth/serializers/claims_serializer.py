from rest_framework.serializers import ModelSerializer
from ..models import Claims


class ClaimsSerializer(ModelSerializer):
    class Meta:
        model = Claims
        fields='__all__'