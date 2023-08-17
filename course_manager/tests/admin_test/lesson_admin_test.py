from django.test import TestCase, Client
from django.urls import reverse
from ..factories import UserFactory, CourseFactory, LessonFactory
from django.contrib.auth import get_user_model
from django.contrib.admin.sites import AdminSite
from course_manager.admin import LessonAdmin
from course_manager.models import Lesson

User = get_user_model()


class LessonAdminTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.admin_site = AdminSite()
        self.user = UserFactory(username="admin", is_staff=True, is_superuser=True)
        self.course = CourseFactory(teacher=self.user)
        self.lesson = LessonFactory(course=self.course)
        self.client.login(username="admin", password="password")

    def test_list_display(self):
        lesson_admin = LessonAdmin(Lesson, self.admin_site)
        self.assertEqual(
            list(lesson_admin.list_display), ["name_lesson", "course", "view_time"]
        )

    def test_get_queryset_superuser(self):
        lesson_admin = LessonAdmin(Lesson, self.admin_site)
        request = self.client.get(reverse("admin:course_manager_lesson_changelist"))
        queryset = lesson_admin.get_queryset(request)
        self.assertIn(self.lesson, queryset)

    def test_get_queryset_teacher(self):
        teacher_user = UserFactory(
            username="teacher", password="password", is_staff=True
        )
        course = CourseFactory(teacher=teacher_user)
        lesson = LessonFactory(course=course)
        self.client.login(username="teacher", password="password")
        lesson_admin = LessonAdmin(Lesson, self.admin_site)

        request = self.client.get(reverse("admin:course_manager_lesson_changelist"))
        queryset = lesson_admin.get_queryset(request)

        self.assertIn(lesson, queryset)

    # Add more test cases as needed

    def tearDown(self):
        self.user.delete()
