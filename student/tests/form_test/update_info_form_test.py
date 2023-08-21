from authen.models import User
from django.test import TestCase
from student.forms import UpdateUserInfoForm
from fake import Faker

fake = Faker()


class UpdateUserInfoFormTest(TestCase):
    def test_clean_email_duplicate(self):
        User.objects.create_user(
            username="testuser1", email="test@example.com", password="testpass"
        )

        form_data = {
            "full_name": fake.full_name(),
            "email": fake.email(),
            "date_of_birth": fake.date(),
        }

        form = UpdateUserInfoForm(data=form_data)
        self.assertFalse(form.is_valid())

        self.assertEqual(form.errors["__all__"][0], "Email has exist in system")

    def test_clean_email_unique(self):
        form_data = {
            "full_name": "Test User",
            "email": "test@example.com",
            "date_of_birth": "1990-01-01",
        }

        form = UpdateUserInfoForm(data=form_data)

        self.assertTrue(form.is_valid())
