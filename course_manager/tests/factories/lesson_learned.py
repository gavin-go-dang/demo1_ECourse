import factory
from .user import UserFactory
from .lesson import LessonFactory
from course_manager.models import LessonLearned
from factory.django import DjangoModelFactory


class LessonLearnedFactory(DjangoModelFactory):
    class Meta:
        model = LessonLearned

    student = factory.SubFactory(UserFactory)
    lesson = factory.SubFactory(LessonFactory)
