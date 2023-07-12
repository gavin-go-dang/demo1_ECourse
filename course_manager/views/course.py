from django.views.generic import View
from django.shortcuts import render
from course_manager.models import Course, Lesson, Topic
from django.utils.decorators import method_decorator
from django.db.models import Count
import math


# Create your views here.


class ListCourse(View):
    template_name = "course.html"
    time_to_learn = {"30": 30, "60": 60, "90": 90}
    page_course = 1
    course_per_view = 7

    def get(self, request, *args, **kwargs):
        query = request.GET.get("query", "")
        number_of_lesson = []
        topics = Topic.objects.all()
        number_of_lesson = []
        course_filter = {}
        min_course_page = 1
        if kwargs:
            self.page_course = kwargs["page"]

        if query:
            courses_query = Course.objects.filter(name_course__icontains=query)
            courses = courses & courses_query

        topic_filter = request.GET.get("topic", "")
        if topic_filter and topic_filter != "All":
            course_filter["topic__name_topic"] = topic_filter

        time_learn = int(request.GET.get("time_learning", ""))
        if time_learn:
            course_filter["time_to_learn_ets__lte"] = time_learn
            course_filter["time_to_learn_ets__gt"] = time_learn - 30

        level = request.GET.get("level", "")
        if level:
            course_filter["level"] = level

        courses = Course.objects.filter(**course_filter).annotate(
            number_of_lesson=Count("lesson")
        )

        # divide course to display
        courses_display = courses[
            (self.page_course - 1)
            * self.course_per_view : self.page_course
            * self.course_per_view
        ]
        course_count = math.ceil(float(courses.count()) / self.course_per_view)
        if self.page_course > 4:
            min_course_page = self.page_course - 3

        if self.page_course < course_count - 3:
            max_course_page = self.page_course + 4
        else:
            max_course_page = course_count + 1

        page_range = range(min_course_page, max_course_page)
        context = {
            "courses": courses_display,
            "topics": topics,
            "current_page": self.page_course,
            "page_range": page_range,
        }
        return render(request, self.template_name, context)
