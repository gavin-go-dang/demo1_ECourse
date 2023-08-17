from django.test import TestCase, Client
from .course import CourseFactory
from course_manager.models import Question
from .exam import ExamFactory
import factory
from faker import Faker

fake = Faker()


class QuestionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Question

    question_text = fake.bothify(letters="ABCDEFGH")
    exam = factory.SubFactory(ExamFactory)
    choice_1 = fake.bothify(letters="ABCDEFGH")
    choice_2 = fake.bothify(letters="ABCDEFGH")
    choice_3 = fake.bothify(letters="ABCDEFGH")
    choice_4 = fake.bothify(letters="ABCDEFGH")
    answer = fake.bothify(letters="ABCDEFGH")
