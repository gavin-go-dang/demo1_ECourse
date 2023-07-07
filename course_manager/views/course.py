from django.views.generic import View
from django.shortcuts import render
from course_manager.models import Course, Lesson, Topic
from django.utils.decorators import method_decorator

# Create your views here.


class ListCourse(View):
    template_name = "course.html"
    time_to_learn = {"1": 30, "2": 60, "3": 90}

    def get(self, request):
        query = request.GET.get("query", "")
        number_of_lesson = []
        topics = Topic.objects.all()
        number_of_lesson = []
        course_filter = {}

        if query:
            courses_query = Course.objects.filter(name_course__icontains=query)
            courses = courses & courses_query

        topic_filter = request.GET.get("topic", "")
        if topic_filter and topic_filter != "All":
            course_filter["topic__name_topic"] = Topic.objects.get(
                name_topic=topic_filter
            )

        time_learn = request.GET.get("time_learning", "")
        if time_learn:
            course_filter["time_to_learn_ets__lte"] = self.time_to_learn[time_learn]
            course_filter["time_to_learn_ets__gt"] = self.time_to_learn[time_learn] - 30

        level = request.GET.get("level", "")
        if level:
            course_filter["level"] = level

        courses = Course.objects.filter(**course_filter)

        for course in courses:
            count = len(Lesson.objects.filter(course=course))
            number_of_lesson.append(count)

        context = {"courses": zip(courses, number_of_lesson), "topics": topics}
        return render(request, self.template_name, context)
