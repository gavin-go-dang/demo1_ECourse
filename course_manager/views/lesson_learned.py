from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from course_manager.models import LessonLearned
from course_manager.serializers import LessonLearnedSerializer
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from rest_framework import status


class LessonLearnedView(APIView):
    renderer_classes = [JSONRenderer]

    def post(self, request, format=None):
        serializer = LessonLearnedSerializer(data=request.data)
        breakpoint()
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        lesson_learned = LessonLearned.objects.all()
        serializer = LessonLearnedSerializer(lesson_learned, many=True)
        return Response(serializer.data)
