import copy

from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import View

from common.views import DetailLoginRequired, LoginRequired

from django.template.loader import render_to_string
from django.conf import settings
from django.core.mail import send_mail, EmailMultiAlternatives
from django.core.mail import get_connection

from course_manager.models import (
    Course,
    Exam,
    Lesson,
    LessonLearned,
    Question,
    ResultTest,
)


class ExamContent(DetailLoginRequired):
    template_name = "exam.html"
    model = Exam

    def get_context_data(self, **kwargs):
        context = super(ExamContent, self).get_context_data(**kwargs)
        context["questions"] = Question.objects.filter(exam=context["object"])
        return context

    def post(self, request, **kwargs):
        correct = 0
        total = 0
        mark = 0
        pass_exam = False
        exam_id = self.kwargs["pk"]
        student = self.request.user
        questions = Question.objects.filter(exam__id=exam_id)
        data = request.POST.dict()
        min_score_to_pass = 7.5
        try:
            del data["csrfmiddlewaretoken"]
        except:
            pass

        list_question = data.keys()
        for index, value in data.items():
            if value == questions.get(id=int(index)).answer:
                correct += 1
            total += 1
        mark = correct / total * 10
        exam = Exam.objects.get(id=exam_id)

        last_test = ResultTest.objects.filter(exam=exam, student=student)
        if last_test:
            number_of_test = last_test.last().number_of_test + 1
        else:
            number_of_test = 1

        if mark > min_score_to_pass:
            pass_exam = True
        else:
            pass_exam = False
        result = ResultTest(
            student=student,
            exam=exam,
            student_answer=data,
            mark=mark,
            number_of_test=number_of_test,
            pass_exam=pass_exam,
        )

        result.save()

        path_to_html = "exam_result.html"

        s = "The result of {} exam".format(exam)
        if pass_exam:
            m = "Congratulations! You have passed the exam!"
        else:
            m = "Sorry! You must do the exam again!"

        time = result.created_at
        context = {
            "title": s,
            "message": m,
            "student": student,
            "course": exam.course,
            "exam": exam,
            "mark": mark,
            "pass_exam": pass_exam,
            "time": time,
            "id": result.id,
        }

        html = render_to_string(path_to_html, context)
        send_mail(
            message=s,
            subject="Exam result",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[student.email],
            html_message=html,
        )

        return redirect(reverse("result", args=[result.id]))
