from django.test import TestCase, Client
from course_manager.models import Topic
from ..factories import TopicFactory
import factory
from faker import Faker


fake = Faker()


class TopicModelTest(TestCase):
    def test_exam_str(self):
        topic = TopicFactory()

        expected_str = topic.name_topic
        self.assertEqual(str(topic), expected_str)
