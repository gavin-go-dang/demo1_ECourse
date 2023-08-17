from django.test import TestCase, Client, RequestFactory
from django.urls import reverse
from authen.models import User
from factory.django import DjangoModelFactory
from authen.views import LoginView
from factory import Faker


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = Faker("user_name")
    password = Faker("password")


class LoginViewTest(TestCase):
    user_data = UserFactory.build(username="gavin", password="pwd")
    factory = RequestFactory()

    def setUp(self):
        self.client = Client()
        self.login_url = reverse("login")
        self.user = User.objects.create_user(
            username=self.user_data.username, password=self.user_data.password
        )

    def test_login_view_get(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "login.html")

    def test_login_failure(self):
        response = self.client.post(
            self.login_url,
            {"username": self.user_data.username, "password": "wrongpassword"},
        )
        self.assertTemplateUsed(response, "login.html")
        self.assertContains(response, "Invalid username or password")

    def test_login_success(self):
        response = self.client.post(
            self.login_url,
            {"username": self.user_data.username, "password": self.user_data.password},
        )
        self.assertEqual(response.status_code, 302)

    def test_authenticated_user_redirect(self):
        # Tạo request với người dùng đã đăng nhập và gọi view
        request = self.factory.get("login")
        request.user = self.user
        response = LoginView.as_view()(request)

        # Kiểm tra kết quả trả về
        self.assertEqual(response.status_code, 302)
