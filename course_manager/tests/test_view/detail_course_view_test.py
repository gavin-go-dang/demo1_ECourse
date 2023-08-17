from django.test import TestCase, RequestFactory, Client
from authen.models import User
from django.shortcuts import redirect, render
from course_manager.models import Course, Lesson, Register
from course_manager.views import DetailCourse


class DetailCourseViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username="testuser", password="testpass")

    def test_get_not_registered(self):
        # Tạo một khóa học
        course = Course.objects.create(name_course="Test Course")

        # Tạo request và gọi view
        request = self.factory.get("/course/1/")
        request.user = self.user
        response = DetailCourse.as_view()(request, id=course.id)

        # Kiểm tra kết quả trả về
        self.assertEqual(response.status_code, 200)

    def test_get_registered(self):
        # Tạo một khóa học
        course = Course.objects.create(name_course="Test Course")

        # Đăng ký khóa học cho người dùng
        Register.objects.create(course=course, student=self.user)

        # Tạo request và gọi view
        request = self.factory.get("/course/1/")
        request.user = self.user
        response = DetailCourse.as_view()(request, id=course.id)

        # Kiểm tra kết quả trả về
        self.assertEqual(response.status_code, 200)
        # self.assertEqual(len(response.content.decode['lessons']), 0)
        # self.assertTrue(response.content.decode['is_register'])

    def test_get_redirect(self):
        # Tạo request và gọi view với tham số access
        request = self.factory.get("/course/1/?access=1")
        request.user = self.user
        response = DetailCourse.as_view()(request, id=1)

        # Kiểm tra kết quả trả về
        self.assertEqual(response.status_code, 302)
