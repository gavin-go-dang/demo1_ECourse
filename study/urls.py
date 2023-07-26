from django.urls import path, include
from .views import LessonContent

urlpatterns = [
    path("lesson/<pk>/", LessonContent.as_view(), name="lesson"),
]
