from django.test import TestCase
from django.contrib.admin.sites import AdminSite
from django.contrib.auth import get_user_model
from factory.django import DjangoModelFactory
from factory import SubFactory
from course_manager.models import Course, Exam
from course_manager.admin import ExamAdmin

User = get_user_model()


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User


class CourseFactory(DjangoModelFactory):
    class Meta:
        model = Course


class ExamFactory(DjangoModelFactory):
    class Meta:
        model = Exam


class ExamAdminTest(TestCase):
    def setUp(self):
        self.superuser = UserFactory(username="admin", is_superuser=True, is_staff=True)
        self.client.login(username="admin", password="password")

        self.site = AdminSite()
        self.exam_admin = ExamAdmin(Exam, self.site)

        self.course = CourseFactory(teacher=self.superuser)

    def test_exam_admin_list_display(self):
        exam = ExamFactory(
            course=self.course, name_exam="Test Exam", description="Description"
        )

        list_display = self.exam_admin.get_list_display(self.request)

        self.assertIn("name_exam", list_display)
        self.assertIn("course", list_display)
        self.assertIn("description", list_display)

    def test_exam_admin_list_filter(self):
        list_filter = self.exam_admin.get_list_filter(self.request)

        self.assertIn(ExamFilterByCourse, list_filter)

    def test_exam_admin_formfield_for_foreignkey(self):
        db_field = Exam._meta.get_field("course")
        request = self.request

        field = self.exam_admin.formfield_for_foreignkey(db_field, request)

        self.assertIsInstance(field, CourseChoiceField)

    def tearDown(self):
        self.client.logout()
