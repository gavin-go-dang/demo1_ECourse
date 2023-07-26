from django.urls import include, path

from .views import StudentProfile

urlpatterns = [
    path("", StudentProfile.as_view(), name="student"),
]
