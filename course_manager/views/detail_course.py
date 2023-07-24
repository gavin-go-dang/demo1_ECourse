from django.views.generic import View
from django.shortcuts import render
from django.views.generic import TemplateView
from common.views import LoginRequired
from course_manager.models import Course, Lesson, Topic, Register
from django.shortcuts import render, redirect


class DetailCourse(LoginRequired, View):
    template_name = "detail_course.html"

    def get(self, request, **kwargs):
        id_course = kwargs.get("id")
        if "access" in request.GET:
            return redirect("home")

        if "register" in request.GET:
            reg = Register.objects.create(
                course=Course.objects.get(id=id_course), student=request.user
            )
            reg.save()

        lessons = Lesson.objects.select_related("course").filter(course__id=id_course)
        if Register.objects.filter(student=request.user).filter(course__id=id_course):
            is_register = True
        else:
            is_register = False
        context = {"lessons": lessons, "is_register": is_register}
        return render(request, self.template_name, context)

        lessons = Lesson.objects.select_related("course").filter(course__id=id_course)

        context = {"lessons": lessons}
        return render(request, self.template_name, context)
