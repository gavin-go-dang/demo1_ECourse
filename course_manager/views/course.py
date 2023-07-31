import math

from django.conf import settings
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Count
from django.shortcuts import render
from django.views.generic import ListView, View

from course_manager.models import Course, Lesson, Topic

# Create your views here.


class ListCourse(View):
    template_name = "course.html"
    time_to_learn = {"30": 30, "60": 60, "90": 90}
    page_course = 1
    paginate_by = settings.PAGAINATION_BY

    def get(self, request, *args, **kwargs):
        query = request.GET.get("query", "")
        number_of_lesson = []
        topics = Topic.objects.all()
        number_of_lesson = []
        course_filter = {}
        courses = Course.objects.all()
        min_course_page = 1
        if kwargs:
            self.page_course = kwargs["page"]

        if query:
            courses_query = Course.objects.filter(name_course__icontains=query)
            courses = courses & courses_query

        topic_filter = request.GET.get("topic", "")
        if topic_filter and topic_filter != "All":
            course_filter["topic__name_topic"] = topic_filter

        time_learn = request.GET.get("time_learning", "")

        if time_learn:
            course_filter["time_to_learn_ets__lte"] = float(time_learn)
            course_filter["time_to_learn_ets__gt"] = float(time_learn) - 30

        level = request.GET.get("level", "")
        if level:
            course_filter["level"] = level

        courses_list = courses.filter(**course_filter).order_by("-register")

        paginator = Paginator(courses_list, self.paginate_by)
        page_number = request.GET.get("page")

        course_obj = paginator.get_page(page_number)
        context = {
            "courses": course_obj,
            "topics": topics,
            "current_page": self.page_course,
            "max_page": paginator.num_pages,
        }

        return render(request, self.template_name, context)
