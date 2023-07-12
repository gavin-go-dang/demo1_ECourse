from django.urls import path, include
from .views import SummaryLearning, ListCourse, DetailCourse


urlpatterns = [
    path("summary/", SummaryLearning.as_view(), name="summary"),
    path("detail/<int:id>/", DetailCourse.as_view(), name="detail_course"),
    path("", ListCourse.as_view(), name="course"),
    path("<int:page>/", ListCourse.as_view(), name="course_page"),
]
