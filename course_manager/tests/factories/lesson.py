from django.test import TestCase, Client
from .course import CourseFactory
from course_manager.models import Lesson
import factory
from faker import Faker

fake = Faker()


class LessonFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Lesson

    name_lesson = fake.name()
    course = factory.SubFactory(CourseFactory)
