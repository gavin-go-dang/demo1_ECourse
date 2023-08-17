from django.test import TestCase, Client
from django.urls import reverse
from course_manager.tests.factories import (
    LessonFactory,
    ExamFactory,
    LessonLearnedFactory,
    UserFactory,
    CourseFactory,
)
from study.views import LessonContent
from course_manager.models import Lesson, Exam


class LessonContentTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.student = UserFactory(username="teststudent")
        self.course = CourseFactory()
        self.lesson = LessonFactory(course=self.course)
        self.exam = ExamFactory(course=self.course)
        self.lesson_learned = LessonLearnedFactory(
            student=self.student, lesson=self.lesson
        )
        self.template_name = "lesson.html"
        self.url = reverse("lesson", kwargs={"pk": self.lesson.id})

    def test_get_lesson_content(self):
        self.client.login(username="teststudent", password="password")
        response = self.client.get(self.url, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, self.template_name)

    def test_lesson_context(self):
        self.client.login(username="teststudent", password="password")
        response = self.client.get(self.url)

        # Kiểm tra rằng response context có đúng các key và giá trị mà bạn mong đợi.
        self.assertEqual(response.context["object"], self.lesson)
        self.assertEqual(
            response.context["lessons"].count(),
            Lesson.objects.filter(course=self.course).count(),
        )
        self.assertEqual(
            response.context["lesson_complete"].count(), 1
        )  # Chú ý kiểm tra dựa trên dữ liệu bạn đã tạo ở trên
        self.assertEqual(
            response.context["lesson_incomplete"].count(),
            Lesson.objects.filter(course=self.course).count() - 1,
        )
        self.assertEqual(
            response.context["exams"].count(),
            Exam.objects.filter(course=self.course).count(),
        )

    def tearDown(self):
        self.course.delete()
        self.lesson.delete()
        self.exam.delete()
        self.lesson_learned.delete()
