from django.test import TestCase, Client
from django.urls import reverse
from course_manager.tests.factories import ResultTestFactory, UserFactory
from course_manager.models import ResultTest
from study.views import ListResultExam


class ListResultExamTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse("list_result")
        self.student = UserFactory(username="teststudent")
        self.client.login(username="teststudent", password="password")

    def test_get_list_result(self):
        result_test = ResultTestFactory(student=self.student)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "list_result.html")
        self.assertIn(result_test, response.context["object_list"])
