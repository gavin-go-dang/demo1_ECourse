import pickle
import zlib

from django.conf import settings
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.views import View
from weasyprint import HTML
from xhtml2pdf import pisa

from authen.models import User
from course_manager.models import Certificate, Course

from .process import html_to_pdf


class GenerateCertificatePdf(View):
    def get(self, request, *args, **kwargs):
        id_course = kwargs.get("course")
        id_student = kwargs.get("student")
        student = User.objects.get(id=id_student)
        course = Course.objects.get(id=id_course)

        data = Certificate.objects.get(course=course, student=id_student)
        id = zlib.adler32(pickle.dumps(data))
        context = {"data": data, "id": id}

        html_string = render_to_string("pdf_certificate.html", context=context)
        html = HTML(string=html_string, base_url=request.build_absolute_uri())
        pdf = html.write_pdf()

        response = HttpResponse(pdf, content_type="application/pdf")
        response["Content-Disposition"] = 'filename="certificate.pdf"'
        return response
