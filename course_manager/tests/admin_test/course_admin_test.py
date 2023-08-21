from django.test import TestCase, Client
from django.urls import reverse
from ..factories import UserFactory, CourseFactory
from django.contrib.auth import get_user_model
from django.contrib.admin.sites import AdminSite
from course_manager.admin import CourseAdmin
from course_manager.models import Course

User = get_user_model()


class CourseAdminTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.admin_site = AdminSite()
        self.user = UserFactory(username="admin", is_staff=True, is_superuser=True)
        self.course = CourseFactory(teacher=self.user)
        self.client.login(username="admin", password="password")

    def test_list_display(self):
        course_admin = CourseAdmin(Course, self.admin_site)
        self.assertEqual(
            list(course_admin.list_display),
            [
                "name_course",
                "topic",
                "register",
                "teacher",
                "time_to_learn_ets",
                "level",
            ],
        )

    def test_get_queryset_superuser(self):
        course_admin = CourseAdmin(Course, self.admin_site)
        url = reverse("admin:course_manager_course_changelist")
        request = self.client.get(url)
        queryset = course_admin.get_queryset(request)
        self.assertIn(self.course, queryset)

    def test_get_queryset_teacher(self):
        teacher_user = UserFactory(username="teacher", is_staff=True)
        course = CourseFactory(teacher=teacher_user)
        self.client.login(username="teacher", password="password")
        course_admin = CourseAdmin(Course, self.admin_site)
        url = reverse("admin:course_manager_course_changelist")
        request = self.client.get(url)
        queryset = course_admin.get_queryset(request)
        self.assertIn(course, queryset)

    # Add more test cases as needed

    def tearDown(self):
        self.user.delete()
