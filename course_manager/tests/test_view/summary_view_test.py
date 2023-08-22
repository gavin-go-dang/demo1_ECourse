from django.test import TestCase, Client
from django.urls import reverse
from course_manager.tests.factories import (
    LessonFactory,
    ResultTestFactory,
    UserFactory,
    RegisterFactory,
    LessonLearnedFactory,
    CourseFactory,
)
from course_manager.views import SummaryLearning


class SummaryLearningTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.student = UserFactory(username="teststudent")
        self.course = CourseFactory()
        self.register = RegisterFactory(student=self.student, course=self.course)
        self.lesson = LessonFactory(course=self.course)
        self.lesson_learned = LessonLearnedFactory(
            student=self.student, lesson=self.lesson
        )
        self.result_test = ResultTestFactory(student=self.student)
        self.template_name = "summary.html"
        self.url = reverse("summary")

    def test_get_summary_learning(self):
        self.client.login(username="teststudent", password="password")
        response = self.client.get(self.url, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, self.template_name)

    def test_summary_context(self):
        self.client.login(username="teststudent", password="password")
        response = self.client.get(self.url)

        self.assertEqual(response.context["courses"].count(), 1)
        self.assertEqual(response.context["object_list"].count(), 1)

    def tearDown(self):
        self.course.delete()
        self.register.delete()
        self.lesson.delete()
        self.lesson_learned.delete()
        self.result_test.delete()
