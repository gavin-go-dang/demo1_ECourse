from authen.models import User
from django.test import TestCase
from student.forms import UpdateUserInfoForm


class UpdateUserInfoFormTest(TestCase):
    def test_clean_email_duplicate(self):
        # Tạo một người dùng mẫu với email đã tồn tại
        User.objects.create_user(
            username="testuser1", email="test@example.com", password="testpass"
        )

        # Tạo dữ liệu cho form
        form_data = {
            "full_name": "Test User",
            "email": "test@example.com",
            "date_of_birth": "1990-01-01",
        }

        form = UpdateUserInfoForm(data=form_data)
        self.assertFalse(form.is_valid())

        self.assertEqual(form.errors["__all__"][0], "Email has exist in system")

    def test_clean_email_unique(self):
        # Tạo dữ liệu cho form
        form_data = {
            "full_name": "Test User",
            "email": "test@example.com",
            "date_of_birth": "1990-01-01",
        }

        form = UpdateUserInfoForm(data=form_data)

        # Kiểm tra rằng form hợp lệ
        self.assertTrue(form.is_valid())
