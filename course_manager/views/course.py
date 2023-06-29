from django.views.generic import View
from django.shortcuts import render
from course_manager.models import Course, Lesson

# Create your views here.


class ListCourse(View):
    template_name = "course.html"

    def get(self, request):
        courses = Course.objects.all()
        number_of_lesson = []
        for course in courses:
            count = len(Lesson.objects.filter(course=course))
            number_of_lesson.append(count)
        context = {"courses": zip(courses, number_of_lesson)}
        return render(request, self.template_name, context)
