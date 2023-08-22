from django.test import TestCase, Client, RequestFactory
from django.urls import reverse
from course_manager.models import Lesson
from course_manager.tests.factories import (
    LessonFactory,
    ExamFactory,
    LessonLearnedFactory,
    UserFactory,
)
from course_manager.views import LessonLearnedView


class LessonContentTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.factory = RequestFactory()
        self.lesson = LessonFactory()
        self.student = UserFactory(username="teststudent")
        self.exam = ExamFactory(course=self.lesson.course)
        self.lesson_learned = LessonLearnedFactory(
            student=self.student, lesson=self.lesson
        )
        self.template_name = "lesson.html"
        self.url = reverse("lesson_student", kwargs={"pk": self.lesson.id})

    def test_get_lesson_content(self):
        request = self.factory.get(self.url)
        response = LessonContent.as_view()(request, pk=self.lesson.id)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, self.template_name)

    def test_lesson_context(self):
        request = self.factory.get(self.url)
        response = LessonContent.as_view()(request, pk=self.lesson.id)
        lesson_content_view = LessonContent()
        lesson_content_view.setup(request, pk=self.lesson.id)
        context = lesson_content_view.get_context_data()
        self.assertEqual(response.context["lessons"], context["lessons"])
        self.assertEqual(
            response.context["lesson_complete"], context["lesson_complete"]
        )
        self.assertEqual(
            response.context["lesson_incomplete"], context["lesson_incomplete"]
        )
        self.assertEqual(response.context["exams"], context["exams"])
        self.assertEqual(response.context["domain"], context["domain"])

    def tearDown(self):
        self.lesson.delete()
        self.exam.delete()
        self.lesson_learned.delete()
