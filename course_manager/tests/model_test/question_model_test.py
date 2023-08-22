from django.test import TestCase
from course_manager.models import Exam, Course, Question
import factory
from faker import Faker
from ..factories import QuestionFactory


fake = Faker()


class ExamModelTest(TestCase):
    def test_exam_str(self):
        question = QuestionFactory()

        expected_str = question.question_text
        self.assertEqual(str(question), expected_str)
