from django.shortcuts import redirect, render
from django.views.generic import View
from django.views.generic.detail import DetailView, View
import copy

from common.views import LoginRequired
from course_manager.models import (
    Course,
    Lesson,
    LessonLearned,
    Exam,
    Question,
    ResultTest,
)


class ExamContent(LoginRequired, DetailView):
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
        exam_id = self.kwargs["pk"]
        student = self.request.user
        questions = Question.objects.filter(exam__id=exam_id)
        data = request.POST.dict()
        del data["csrfmiddlewaretoken"]

        list_question = data.keys()
        for index, value in data.items():
            if value == questions.get(id=int(index)).answer:
                correct += 1
            total += 1
        mark = correct / total * 10
        exam = Exam.objects.get(id=exam_id)

        number_of_test = (
            ResultTest.objects.filter(exam=exam, student=student).last().number_of_test
            + 1
        )

        if not number_of_test:
            number_of_test = 1

        result = ResultTest(
            student=student,
            exam=exam,
            student_answer=data,
            mark=mark,
            number_of_test=number_of_test,
        )

        breakpoint()
        result.save()
        return redirect("/study/exam/1")
