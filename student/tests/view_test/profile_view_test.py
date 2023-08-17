from django.test import TestCase, Client
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from django.contrib.auth import get_user_model
from course_manager.tests.factories import (
    UserFactory,
    CertificateFactory,
    RegisterFactory,
    CourseFactory,
)
from student.forms import UpdateUserInfoForm, CoverImgForm
from course_manager.models import Certificate, Register


class StudentProfileViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse("student")
        self.user = UserFactory.create(username="student1")
        self.client.force_login(self.user)

    def test_get_student_profile(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "student_info.html")

    def test_post_update_info_valid_form(self):
        completed_course = CertificateFactory.create(student=self.user)
        registered_course = RegisterFactory.create(student=self.user)

        form_data = {
            "update": "Update",
            "full_name": "New Full Name",
            "email": "newemail@example.com",
            "date_of_birth": "1990-01-01",
        }
        response = self.client.post(self.url, data=form_data)
        self.assertEqual(
            response.status_code, 302
        )  # Chuyển hướng sau khi cập nhật thành công

        # Kiểm tra xem thông tin người dùng đã được cập nhật chưa
        updated_user = get_user_model().objects.get(id=self.user.id)
        self.assertEqual(updated_user.full_name, "New Full Name")
        self.assertEqual(updated_user.email, "newemail@example.com")

    def test_post_update_info_invalid_form(self):
        form_data = {
            "update": "Update",
            "full_name": "",
            "email": "newemail@example.com",
            "date_of_birth": "1990-01-01",
        }
        response = self.client.post(self.url, data=form_data)
        self.assertEqual(response.status_code, 200)  # Trang sẽ hiển thị lỗi

    def test_post_update_img_valid_form(self):
        img = SimpleUploadedFile("image.jpg", b"image_content")

        form_data = {
            "update_img": "Update Image",
            "avatar": img,
        }
        response = self.client.post(self.url, data=form_data)
        self.assertEqual(response.status_code, 302)

        updated_user = get_user_model().objects.get(id=self.user.id)
        self.assertTrue(updated_user.cover_img.url.startswith("/media/"))
