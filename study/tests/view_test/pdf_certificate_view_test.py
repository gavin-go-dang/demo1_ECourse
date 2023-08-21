from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from course_manager.models import Certificate, Course
from course_manager.tests.factories import (
    UserFactory,
    CertificateFactory,
    CourseFactory,
)
from io import BytesIO

User = get_user_model()


class GenerateCertificatePdfTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.student = UserFactory(username="teststudent")
        self.course = CourseFactory()
        self.certificate = CertificateFactory(student=self.student, course=self.course)
        self.url = reverse(
            "cert_pdf", kwargs={"course": self.course.id, "student": self.student.id}
        )

    def test_generate_certificate_pdf(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response["Content-Type"], "application/pdf")
        self.assertTrue(response.has_header("Content-Disposition"))

        # You can further validate the PDF content if needed
        pdf_content = response.content
        # Perform checks on pdf_content

    def tearDown(self):
        self.student.delete()
        self.course.delete()
        self.certificate.delete()
