from rest_framework import serializers
from .models import LessonLearned
from rest_framework.validators import UniqueTogetherValidator, UniqueValidator


class LessonLearnedSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonLearned
        fields = ("student", "lesson")

        validators = [
            UniqueTogetherValidator(
                queryset=LessonLearned.objects.all(), fields=["student", "lesson"]
            )
        ]
