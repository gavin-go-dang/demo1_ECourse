from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from course_manager.models import Certificate, Course
from course_manager.tests.factories import (
    UserFactory,
    CertificateFactory,
    CourseFactory,
)

import pickle
import zlib


class CheckCertViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.certificate = CertificateFactory()
        self.template_name = "check_cert.html"
        self.url = reverse("check_cert")

    def test_check_existing_certificate(self):
        response = self.client.post(
            self.url, {"id": zlib.adler32(pickle.dumps(Certificate.objects.all()[0]))}
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, self.template_name)
        self.assertTrue(response.context["exist"])
        self.assertEqual(response.context["data"], self.certificate)

    def test_check_non_existing_certificate(self):
        non_existing_id = 4444444
        response = self.client.post(self.url, {"id": non_existing_id})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, self.template_name)
        self.assertFalse(response.context["exist"])

    def tearDown(self):
        self.certificate.delete()
