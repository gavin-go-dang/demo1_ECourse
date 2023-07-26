from django.urls import include, path

from .views import LessonContent

urlpatterns = [
    path("lesson/<pk>/", LessonContent.as_view(), name="lesson"),
]
