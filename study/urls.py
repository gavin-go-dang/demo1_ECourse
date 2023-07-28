from django.urls import include, path

from .views import ExamContent, LessonContent, ResultExam

urlpatterns = [
    path("lesson/<pk>/", LessonContent.as_view(), name="lesson"),
    path("exam/<pk>/", ExamContent.as_view(), name="exam"),
    path("result/<pk>/", ResultExam.as_view(), name="result"),
]
