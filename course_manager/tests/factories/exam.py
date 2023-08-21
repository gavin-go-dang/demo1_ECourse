from django.test import TestCase, Client
from course_manager.models import Exam
from .course import CourseFactory
import factory
from faker import Faker

fake = Faker()


class ExamFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Exam

    name_exam = fake.name()
    description = fake.text()
    course = factory.SubFactory(CourseFactory)
