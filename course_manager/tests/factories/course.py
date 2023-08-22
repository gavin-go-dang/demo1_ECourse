from django.test import TestCase, Client
from .topic import TopicFactory
from course_manager.models import Course
import factory
from faker import Faker

fake = Faker()


class CourseFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Course

    name_course = fake.name()
    description = "This is a test course"
    topic = factory.SubFactory(TopicFactory)
