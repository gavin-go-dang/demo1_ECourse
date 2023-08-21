from django.test import TestCase, Client
from course_manager.models import Topic
import factory
from faker import Faker

fake = Faker()


class TopicFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Topic

    name_topic = fake.name()
    description = fake.text()
