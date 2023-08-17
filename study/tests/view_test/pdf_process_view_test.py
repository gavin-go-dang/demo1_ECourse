from django.test import TestCase
from course_manager.tests.factories import ContextFactory
from study.views import html_to_pdf


class HtmlToPdfTest(TestCase):
    def test_html_to_pdf(self):
        context = ContextFactory()

        template = "pdf_certificate.html"
        response = html_to_pdf(template, context)
        self.assertIsNotNone(response)
        self.assertEqual(response["Content-Type"], "application/pdf")
