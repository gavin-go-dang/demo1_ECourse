from django.test import TestCase, Client
from django.urls import reverse
from authen.models import User


class LoginViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.login_url = reverse("login")
        self.username = "gavin"
        self.password = "123"
        self.user = User.objects.create_user(
            username=self.username, password=self.password
        )

    def test_login_view_get(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "login.html")

    def test_login_failure(self):
        response = self.client.post(
            self.login_url, {"username": self.username, "password": "wrongpassword"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "login.html")
        self.assertContains(response, "Invalid username or password")
