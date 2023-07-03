from django.views.generic import View
from django.shortcuts import render
from django.views.generic import TemplateView
from course_manager.models import Course, Lesson, Topic


class DetailCourse(View):
    template_name = "detail_course.html"

    def get(self, request, **kwargs):
        id_course = kwargs.get("id")

        course = Course.objects.get(id=id_course)
        lessons = Lesson.objects.filter(course=course)

        context = {"course": course, "lessons": lessons}

        return render(request, self.template_name, context)
