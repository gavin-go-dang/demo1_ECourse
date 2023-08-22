from django.test import TestCase
from course_manager.models import Exam, Course
from ..factories import ExamFactory
import factory
from faker import Faker


fake = Faker()


class ExamModelTest(TestCase):
    def test_exam_str(self):
        exam = ExamFactory()

        expected_str = "{}-{}".format(exam.name_exam, exam.course.name_course)
        self.assertEqual(str(exam), expected_str)
