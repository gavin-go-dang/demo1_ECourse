from django.test import TestCase, Client
from course_manager.models import Certificate
from .topic import TopicFactory
import factory
from faker import Faker
from ..factories import UserFactory, CourseFactory

fake = Faker()


class CertificateFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Certificate

    student = factory.SubFactory(UserFactory)
    course = factory.SubFactory(CourseFactory)
    score = fake.random_digit_above_two()
