from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import DetailCourse, LessonLearnedView, ListCourse, SummaryLearning

urlpatterns = [
    path("summary/", SummaryLearning.as_view(), name="summary"),
    path("detail/<int:id>/", DetailCourse.as_view(), name="detail_course"),
    path("", ListCourse.as_view(), name="course"),
    path("<int:page>", ListCourse.as_view(), name="course_page"),
    path("lesson_learn", LessonLearnedView.as_view(), name="lesson_student"),
]
urlpatterns = format_suffix_patterns(urlpatterns)
