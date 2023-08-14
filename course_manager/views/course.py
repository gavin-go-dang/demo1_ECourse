import json
import math

from django.conf import settings
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import (
    Case,
    Count,
    F,
    FloatField,
    OuterRef,
    Subquery,
    Sum,
    Value,
    When,
)
from django.db.models.functions import Coalesce, Round
from django.shortcuts import render
from django.views.generic import ListView, TemplateView, View
from webpush import send_user_notification

from common.views import LoginRequired
from course_manager.models import (
    Course,
    Lesson,
    LessonLearned,
    Register,
    ResultTest,
    Topic,
)

# Create your views here.


class ListCourse(LoginRequired, View):
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
        topic_checked = None
        time_checked = None
        level_checked = None
        if kwargs:
            self.page_course = kwargs["page"]

        if query:
            courses_query = Course.objects.filter(name_course__icontains=query)
            courses = courses & courses_query

        topic_filter = request.GET.get("topic", "")
        if topic_filter and topic_filter != "All":
            course_filter["topic__name_topic"] = topic_filter
            topic_checked = topic_filter
        time_learn = request.GET.get("time_learning", "")

        if time_learn:
            course_filter["time_to_learn_ets__lte"] = float(time_learn)
            course_filter["time_to_learn_ets__gt"] = float(time_learn) - 30
            time_checked = time_learn
        level = request.GET.get("level", "")
        if level:
            course_filter["level"] = level
            level_checked = level
        courses_list = courses.filter(**course_filter).order_by("-register")

        # paginator = Paginator(courses_list, self.paginate_by)
        # page_number = request.GET.get("page")

        # course_obj = paginator.get_page(page_number)

        # progress
        progress_courses = (
            Register.objects.filter(student=self.request.user)
            .select_related("course")
            .prefetch_related("course_include")
        )

        total_lessons = (
            Lesson.objects.filter(course_id__in=progress_courses.values("course"))
            .values("course")
            .annotate(total_lessons=Count("id"))
            .values("course", "total_lessons")
        )

        completed_lessons = (
            LessonLearned.objects.filter(student=self.request.user)
            .values("lesson__course")
            .annotate(completed_lessons=Count("id"))
            .values("lesson__course", "completed_lessons")
        )

        course_completion_rate = (
            total_lessons.annotate(
                name_course=F("course__name_course"),
                completed_lessons=Coalesce(
                    Subquery(
                        completed_lessons.filter(
                            lesson__course_id=OuterRef("course")
                        ).values("completed_lessons")[:1]
                    ),
                    0,
                ),
            )
            .annotate(
                course_completion_rate=Round(
                    F("completed_lessons") * 100.0 / F("total_lessons"), 2
                )
            )
            .values("name_course", "course_completion_rate")
        )

        progress_dict = {}
        for item in course_completion_rate:
            name_course = item["name_course"]
            course_completion_rate = item["course_completion_rate"]
            progress_dict[name_course] = course_completion_rate

        for course in courses_list:
            try:
                course.progress = progress_dict.get(
                    course.name_course, progress_dict[course.name_course]
                )
            except:
                course.progress = progress_dict.get(course.name_course, 0)

        paginator = Paginator(courses_list, self.paginate_by)
        page_number = request.GET.get("page")

        course_obj = paginator.get_page(page_number)

        context = {
            "courses": course_obj,
            "topics": topics,
            "current_page": self.page_course,
            "max_page": paginator.num_pages,
            "level_checked": level_checked,
            "time_checked": time_checked,
            "topic_checked": topic_checked,
            "progress": progress_courses,
        }

        return render(request, self.template_name, context)
