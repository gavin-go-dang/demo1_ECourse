from django.views.generic import View
from django.shortcuts import render
from django.views.generic import TemplateView
from course_manager.models import Course, Lesson, Topic


class DetailCourse(View):
    template_name = "detail_course.html"

    def get(self, request, **kwargs):
        id_course = kwargs.get("id")
        lessons = Lesson.objects.select_related("course").filter(course__id=id_course)
        context = {"lessons": lessons}
        print(context)
        return render(request, self.template_name, context)
