from django.test import TestCase, Client
from django.urls import reverse
from course_manager.tests.factories import (
    UserFactory,
    CourseFactory,
    ResultTestFactory,
    CertificateFactory,
    ExamFactory,
)
from course_manager.models import Certificate, ResultTest
from django.contrib.auth import get_user_model
from django.contrib.admin.sites import AdminSite
from study.views import CertificateContent

User = get_user_model()


class CertificateViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.admin_site = AdminSite()
        self.student = UserFactory(username="teststudent")
        self.course = CourseFactory(teacher=self.student)
        self.exam = ExamFactory(course=self.course)
        self.result = ResultTestFactory(student=self.student, exam=self.exam)
        self.certificate = CertificateFactory(student=self.student, course=self.course)
        self.template_name = "certificate.html"

    def test_get_certificate(self):
        url = reverse(
            "cert",
            kwargs={"course": self.course.id, "student": self.student.id},
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, self.template_name)

    def test_certificate_content(self):
        url = reverse(
            "cert",
            kwargs={"course": self.course.id, "student": self.student.id},
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "cert")

    def test_certificate_update(self):
        url = reverse(
            "cert",
            kwargs={"course": self.course.id, "student": self.student.id},
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        updated_cert = Certificate.objects.get(id=self.certificate.id)
        if self.result.mark > updated_cert.score:
            self.assertEqual(updated_cert.score, self.result.mark)

    def tearDown(self):
        self.student.delete()
        self.course.delete()
        self.exam.delete()
        self.result.delete()
        self.certificate.delete()
