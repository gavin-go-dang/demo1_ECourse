from django.test import TestCase
from django.contrib.admin.sites import AdminSite
from course_manager.admin import ResultTestAdmin
from course_manager.models import Course, Exam, ResultTest
from course_manager.tests.factories import (
    UserFactory,
    CourseFactory,
    ExamFactory,
    ResultTestFactory,
)


class ResultTestAdminTest(TestCase):
    def setUp(self):
        self.site = AdminSite()
        self.user = UserFactory(username="testteacher", is_superuser=False)
        self.superuser = UserFactory(username="admin", is_superuser=True)
        self.course = CourseFactory(teacher=self.user)
        self.exam = ExamFactory(course=self.course)
        self.result_test = ResultTestFactory(exam=self.exam)
        self.admin = ResultTestAdmin(ResultTest, self.site)

    def test_result_test_admin_get_queryset_teacher(self):
        # Đảm bảo rằng `get_queryset` chỉ trả về các kết quả bài kiểm tra liên quan đến người dùng hiện tại (giáo viên)
        request = self._create_request(self.user)
        queryset = self.admin.get_queryset(request)
        self.assertIn(self.result_test, queryset)
        self.assertEqual(queryset.count(), 1)

    def test_result_test_admin_get_queryset_superuser(self):
        # Đảm bảo rằng `get_queryset` trả về tất cả các kết quả bài kiểm tra khi được sử dụng bởi một superuser
        request = self._create_request(self.superuser)
        queryset = self.admin.get_queryset(request)
        self.assertIn(self.result_test, queryset)
        self.assertEqual(queryset.count(), 1)

    def _create_request(self, user):
        request = self.client.request().wsgi_request
        request.user = user
        return request
