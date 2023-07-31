from django.views.generic.detail import View
from django.shortcuts import render
from django.db.models import Max, Avg

from course_manager.models import Certificate, Course, Exam, ResultTest
from authen.models import User


class CertificateContent(View):
    template_name = "certificate.html"

    def get(self, request, **kwargs):
        id_course = kwargs.get("course")
        id_student = kwargs.get("student")
        student = User.objects.get(id=id_student)
        course = Course.objects.get(id=id_course)
        result = (
            ResultTest.objects.filter(exam__course=course, student__id=id_student)
            .values("student", "exam")
            .annotate(max_score=Max("mark"))
            .order_by("student", "exam")
        )
        max_score = result.aggregate(Avg("max_score"))["max_score__avg"]
        context = {
            "name": student.full_name,
            "result": result,
            "score": max_score,
            "course": course,
            "date": None,
        }
        if context["score"] == None:
            return render(request, "incomplete.html")
        return render(request, self.template_name, context)
