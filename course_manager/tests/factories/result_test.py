from django.test import TestCase, Client
from course_manager.models import ResultTest
from .course import CourseFactory
from ..factories import UserFactory, ExamFactory
import factory
from faker import Faker

fake = Faker()


class ResultTestFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ResultTest

    student = factory.SubFactory(UserFactory)
    exam = factory.SubFactory(ExamFactory)
    mark = fake.random_digit_above_two()
    student_answer = {
        "1": "The autonomous acquisition of knowledge through the use of computer programs",
        "2": "All of the above",
        "3": "Random Forest",
        "4": "Decision trees are prone to be overfit",
    }
    number_of_test = 1
    pass_exam = True
