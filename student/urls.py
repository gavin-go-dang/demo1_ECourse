from django.urls import path, include
from .views import StudentProfile


urlpatterns = [
    path("", StudentProfile.as_view(), name="student"),
]
