from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from course_manager.tests.factories import UserFactory


class TeacherAdminViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.admin_url = reverse("admin:authen_user_changelist")
        self.user = UserFactory.create(
            username="teacher1",
            email="teacher1@example.com",
            date_of_birth="1990-01-01",
            type="teacher",
        )
        self.superuser = UserFactory.create(
            username="superuser", email="superuser@example.com", is_superuser=True
        )
        self.client.force_login(self.superuser)

    def test_teacher_admin_list_view(self):
        response = self.client.get(self.admin_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "teacher1")
        self.assertContains(response, "teacher1@example.com")
        self.assertContains(response, "teacher")

    def test_teacher_admin_change_view(self):
        change_url = reverse("admin:authen_user_change", args=[self.user.id])
        response = self.client.get(change_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Change user")
        self.assertContains(response, "teacher1")
        self.assertContains(response, "teacher1@example.com")
        self.assertContains(response, "1990-01-01")
        self.assertContains(response, "teacher")

    def test_teacher_admin_add_view(self):
        add_url = reverse("admin:authen_user_add")
        response = self.client.get(add_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Add user")

    def test_teacher_admin_delete_view(self):
        delete_url = reverse("admin:authen_user_delete", args=[self.user.id])
        response = self.client.get(delete_url)
        self.assertEqual(response.status_code, 200)
        # self.assertContains(response, "Delete user")
