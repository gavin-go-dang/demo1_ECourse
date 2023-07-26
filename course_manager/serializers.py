from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator, UniqueValidator

from .models import LessonLearned


class LessonLearnedSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonLearned
        fields = ("student", "lesson")

        validators = [
            UniqueTogetherValidator(
                queryset=LessonLearned.objects.all(), fields=["student", "lesson"]
            )
        ]
