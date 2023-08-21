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
        course = Course.objects.create(name_course="Test Course")

        request = self.factory.get("/course/1/")
        request.user = self.user
        response = DetailCourse.as_view()(request, id=course.id)

        self.assertEqual(response.status_code, 200)

    def test_get_registered(self):
        course = Course.objects.create(name_course="Test Course")

        Register.objects.create(course=course, student=self.user)

        request = self.factory.get("/course/1/")
        request.user = self.user
        response = DetailCourse.as_view()(request, id=course.id)

        self.assertEqual(response.status_code, 200)

    def test_get_redirect(self):
        request = self.factory.get("/course/1/?access=1")
        request.user = self.user
        response = DetailCourse.as_view()(request, id=1)

        self.assertEqual(response.status_code, 302)
