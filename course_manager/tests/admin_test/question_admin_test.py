from django.test import TestCase
from django.contrib.admin.sites import AdminSite
from course_manager.admin import QuestionAdmin
from course_manager.models import Course, Exam, Question
from course_manager.tests.factories import (
    UserFactory,
    CourseFactory,
    ExamFactory,
    QuestionFactory,
)


class QuestionAdminTest(TestCase):
    def setUp(self):
        self.site = AdminSite()
        self.user = UserFactory(username="testteacher", is_superuser=False)
        self.course = CourseFactory(teacher=self.user)
        self.exam = ExamFactory(course=self.course)
        self.question = QuestionFactory(exam=self.exam)
        self.admin = QuestionAdmin(Question, self.site)

    def test_question_admin_get_queryset(self):
        request = self._create_request(self.user)
        queryset = self.admin.get_queryset(request)
        self.assertIn(self.question, queryset)
        self.assertEqual(queryset.count(), 1)

    def test_question_admin_formfield_for_foreignkey(self):
        request = self._create_request(self.user)
        formfield = self.admin.formfield_for_foreignkey(
            Question._meta.get_field("exam"), request
        )
        self.assertIn(self.exam, formfield.queryset)
        self.assertEqual(formfield.queryset.count(), 1)

    def _create_request(self, user):
        request = self.client.request().wsgi_request
        request.user = user
        return request
