from django.test import TestCase
from authen.models import User
from django.utils import timezone
from authen.forms import SignUpForm


# models test
class UserFormTest(TestCase):
    def create_user(
        self,
        username="student123",
        full_name="Brack Obama",
        email="emailtest@gmail.com",
        password="123",
        type="student",
    ):
        return User.objects.create(
            username=username,
            full_name=full_name,
            email=email,
            password=password,
            type=type,
        )

    def test_user_creation(self):
        u = self.create_user()
        self.assertTrue(isinstance(u, User))
        self.assertEqual(u.__str__(), u.username)
