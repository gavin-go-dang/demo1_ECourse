from django.views.generic import View
from django.shortcuts import render
from django.views.generic.detail import DetailView, View
from common.views import LoginRequired
from course_manager.models import Course, Lesson, LessonLearned
from django.shortcuts import render, redirect


class LessonContent(DetailView):
    template_name = "lesson.html"
    model = Lesson

    def get_context_data(self, **kwargs):
        context = super(LessonContent, self).get_context_data(**kwargs)
        context["lessons"] = Lesson.objects.filter(
            course=context["object"].course
        ).order_by("index")
        if context["object"].index != 1:
            context["previous"] = context["object"].id - 1
        if context["object"].index != context["lessons"].last().index:
            context["next"] = context["object"].id + 1

        context["lesson_complete"] = LessonLearned.objects.filter(
            student=self.request.user.id
        )
        context["lesson_incomplete"] = context["lessons"].exclude(
            id__in=context["lesson_complete"].values("lesson")
        )
        return context
