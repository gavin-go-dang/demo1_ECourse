from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from course_manager.models import Exam, Question, ResultTest
from course_manager.tests.factories import (
    ExamFactory,
    QuestionFactory,
    UserFactory,
    CourseFactory,
)
from datetime import datetime
from django.utils import timezone

User = get_user_model()


class ExamViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.student = UserFactory(username="teststudent")
        self.course = CourseFactory(teacher=self.student)

        self.exam = ExamFactory(course=self.course)
        self.question = QuestionFactory(exam=self.exam)

    def test_get_exam_content(self):
        self.client.login(username="teststudent", password="password")
        url = reverse("exam", kwargs={"pk": self.exam.id})
        response = self.client.get(url, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "exam.html")

    def test_post_exam_result(self):
        self.client.login(username="teststudent", password="password")
        url = reverse("exam", kwargs={"pk": self.exam.id})
        data = {str(self.question.id): self.question.answer}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)

        result = ResultTest.objects.get(student=self.student, exam=self.exam)
        self.assertEqual(result.mark, 10)  # Assuming the answer is correct
        self.assertEqual(result.pass_exam, True)  # Assuming the pass condition is met

    def tearDown(self):
        self.student.delete()
        self.exam.delete()
        self.question.delete()
