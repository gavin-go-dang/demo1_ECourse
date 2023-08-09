import logging

from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist
from django.db.models import Avg, Max
from django.shortcuts import render
from django.views.generic.detail import View
from sentry_sdk import capture_exception

from authen.models import User
from course_manager.models import Certificate, Course, Exam, ResultTest


class CertificateContent(View):
    template_name = "certificate.html"

    def get(self, request, **kwargs):
        id_course = kwargs.get("course")
        id_student = kwargs.get("student")
        student = User.objects.get(id=id_student)
        course = Course.objects.get(id=id_course)
        result = (
            ResultTest.objects.prefetch_related("exam__course__id", "student__id")
            .filter(exam__course__id=id_course, student__id=id_student)
            .values("student", "exam")
            .annotate(max_score=Max("mark"))
            .order_by("student", "exam")
        )
        max_avg_score = result.aggregate(Avg("max_score"))["max_score__avg"]

        try:  # 1 record
            cert = Certificate.objects.get(student=student, course=course)
            if cert.score < max_avg_score:
                cert.score = max_avg_score
                cert.save()
        except ObjectDoesNotExist as e:  # Not exist
            try:
                cert = Certificate(student=student, course=course, score=max_avg_score)
                cert.save()
            except:
                return render(request, "incomplete.html")
        except Exception as e:  # Multire
            # capture_exception(e)
            pass

        context = {
            "name": student,
            "result": result,
            "score": max_avg_score,
            "course": course,
            "date": cert.created_at.strftime("%Y-%m-%d"),
        }
        breakpoint()
        if context["score"] == None:
            return render(request, "incomplete.html")
        return render(request, self.template_name, context)
