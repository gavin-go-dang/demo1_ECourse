from django.test import TestCase, Client
from .course import CourseFactory
from .user import UserFactory
from course_manager.models import Register
import factory
from faker import Faker

fake = Faker()


class RegisterFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Register

    student = factory.SubFactory(UserFactory)
    course = factory.SubFactory(CourseFactory)
