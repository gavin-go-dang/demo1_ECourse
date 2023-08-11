from django.shortcuts import redirect, render
from django.views.generic import View

from common.views import DetailLoginRequired
from course_manager.models import Course, Exam, Lesson, LessonLearned
from django.conf import settings


class LessonContent(DetailLoginRequired):
    template_name = "lesson.html"
    model = Lesson

    def get_context_data(self, **kwargs):
        context = super(LessonContent, self).get_context_data(**kwargs)
        course = context["object"].course
        context["lessons"] = Lesson.objects.filter(course=course).order_by("index")
        if context["object"].index != 1:
            context["previous"] = context["object"].id - 1
        if context["object"].index != context["lessons"].last().index:
            context["next"] = context["object"].id + 1

        context["lesson_complete"] = LessonLearned.objects.filter(
            student=self.request.user.id, lesson__course=course
        )
        context["lesson_incomplete"] = context["lessons"].exclude(
            id__in=context["lesson_complete"].values("lesson")
        )
        context["exams"] = Exam.objects.filter(course=course)
        context["domain"] = settings.DOMAIN
        return context
