from django.urls import path, include
from .views import SummaryLearning, ListCourse


urlpatterns = [
    path("summary/", SummaryLearning.as_view(), name="summary"),
    path("", ListCourse.as_view(), name="course"),
]
