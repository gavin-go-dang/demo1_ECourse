from authen.models import User
from django.test import TestCase, Client
from django.urls import reverse
from factory.django import DjangoModelFactory
from factory import Faker


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = Faker("user_name")
    full_name = Faker("name")
    email = Faker("email")
    password = Faker("password")
    type = Faker("random_element", elements=["student", "teacher"])


class RegisterViewTest(TestCase):
    fixtures = ["data_sample.json"]

    user_data = UserFactory.build(
        username="testuser",
        full_name="abc xyz",
        password="testpassword",
        email="abcdfg@gmail.com",
        type="student",
    )

    def setUp(self):
        self.client = Client()
        self.register_url = reverse("register")

    def test_register_success(self):
        user_data = UserFactory.build(
            username=fake.name(),
            full_name=fake.full_name(),
            password="testpassword",
            email=fake.email(),
            type="student",
        )

        response = self.client.post(
            self.register_url,
            {
                "username": user_data.username,
                "full_name": user_data.full_name,
                "email": user_data.email,
                "password": user_data.password,
                "confirm_password": user_data.password,
                "type": user_data.type,
            },
        )

        self.assertRedirects(response, reverse("login"))
        user_exists = User.objects.filter(username=user_data.username).exists()
        self.assertTrue(user_exists)

    def test_register_failure_username(self):
        create_user_1 = self.client.post(
            self.register_url,
            {
                "username": self.user_data.username,
                "full_name": self.user_data.full_name,
                "email": "abcdzx@gmaill.com",
                "password": self.user_data.password,
                "confirm_password": self.user_data.password,
                "type": self.user_data.type,
            },
        )
        response = self.client.post(
            self.register_url,
            {
                "username": self.user_data.username,
                "full_name": self.user_data.full_name,
                "email": "othersemail@gmaill.com",
                "password": self.user_data.password,
                "confirm_password": self.user_data.password,
                "type": self.user_data.type,
            },
        )
        self.assertTemplateUsed(response, "registeration.html")
        self.assertContains(response, "Username is exist")

    def test_register_failure_email(self):
        create_user_1 = self.client.post(
            self.register_url,
            {
                "username": self.user_data.username,
                "full_name": self.user_data.full_name,
                "email": self.user_data.email,
                "password": self.user_data.password,
                "confirm_password": self.user_data.password,
                "type": self.user_data.type,
            },
        )
        response = self.client.post(
            self.register_url,
            {
                "username": "others username",
                "full_name": self.user_data.full_name,
                "email": self.user_data.email,
                "password": self.user_data.password,
                "confirm_password": self.user_data.password,
                "type": self.user_data.type,
            },
        )
        self.assertTemplateUsed(response, "registeration.html")
        self.assertContains(response, "Email is exist")

    def test_teacher_register_success(self):
        user_data = UserFactory.build(
            username="testteacher",
            full_name="abc xyz",
            password="testpassword",
            email="abcdfg@gmail.com",
            type="teacher",
        )

        response = self.client.post(
            self.register_url,
            {
                "username": user_data.username,
                "full_name": user_data.full_name,
                "email": user_data.email,
                "password": user_data.password,
                "confirm_password": user_data.password,
                "type": user_data.type,
            },
            follow=True,
        )

        self.assertTemplateUsed(response, "material/admin/login.html")
        user_exists = User.objects.filter(username=user_data.username).exists()
        self.assertTrue(user_exists)
