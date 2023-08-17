from authen.models import User
from django.test import TestCase, Client
from django.urls import reverse


class RegisterViewTest(TestCase):
    fixtures = ["data_sample.json"]

    def setUp(self):
        self.client = Client()
        self.register_url = reverse("register")
        self.username = "testuser"
        self.full_name = "abc xyz"
        self.password = "testpassword"
        self.email = "abcdfg@gmail.com"
        self.type = "student"

    def test_register_success(self):
        response = self.client.post(
            self.register_url,
            {
                "username": self.username,
                "full_name": self.full_name,
                "email": self.email,
                "password": self.password,
                "confirm_password": self.password,
                "type": self.type,
            },
        )

        self.assertRedirects(response, reverse("login"))

        # Assert that the user was created and can now log in
        user_exists = User.objects.filter(username=self.username).exists()
        self.assertTrue(user_exists)

    def test_register_failure_username(self):
        create_user_1 = self.client.post(
            self.register_url,
            {
                "username": self.username,
                "full_name": self.full_name,
                "email": "abcdzx@gmaill.com",
                "password": self.password,
                "confirm_password": self.password,
                "type": self.type,
            },
        )
        response = self.client.post(
            self.register_url,
            {
                "username": self.username,
                "full_name": self.full_name,
                "email": "othersemail@gmaill.com",
                "password": self.password,
                "confirm_password": self.password,
                "type": self.type,
            },
        )
        self.assertTemplateUsed(response, "registeration.html")
        self.assertContains(response, "Username is exist")

    def test_register_failure_email(self):
        create_user_1 = self.client.post(
            self.register_url,
            {
                "username": self.username,
                "full_name": self.full_name,
                "email": self.email,
                "password": self.password,
                "confirm_password": self.password,
                "type": self.type,
            },
        )
        response = self.client.post(
            self.register_url,
            {
                "username": "others username",
                "full_name": self.full_name,
                "email": self.email,
                "password": self.password,
                "confirm_password": self.password,
                "type": self.type,
            },
        )
        self.assertTemplateUsed(response, "registeration.html")
        self.assertContains(response, "Email is exist")
