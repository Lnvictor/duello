from rest_framework import ModelSerializer

from duello.cage.models import Question


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__
