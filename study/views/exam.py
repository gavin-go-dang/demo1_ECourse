import copy

from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import View

from common.views import DetailLoginRequired, LoginRequired
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
        ass_exam = False
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

        last_test = ResultTest.objects.filter(exam=exam, student=student)
        if last_test:
            number_of_test = last_test.last().number_of_test + 1
        else:
            number_of_test = 1

        if mark > 7.5:
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
        breakpoint()

        result.save()
        return redirect(reverse("result", args=[result.id]))
