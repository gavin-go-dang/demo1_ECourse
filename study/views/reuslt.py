from django.shortcuts import redirect, render
from django.views.generic import View

from common.views import DetailLoginRequired, LoginRequired
from course_manager.models import Course, Lesson, LessonLearned, Question, ResultTest


class ResultExam(DetailLoginRequired):
    template_name = "result.html"
    model = ResultTest

    def get_context_data(self, **kwargs):
        context = super(ResultExam, self).get_context_data(**kwargs)
        answers = context["object"].student_answer.values()
        context["results"] = zip(
            Question.objects.filter(exam=context["object"].exam.id), answers
        )
        # breakpoint()
        return context
