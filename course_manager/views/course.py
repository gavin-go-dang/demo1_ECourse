from django.views.generic import View
from django.shortcuts import render
from course_manager.models import Course, Lesson, Topic

# Create your views here.


class ListCourse(View):
    template_name = "course.html"

    def get(self, request):
        query = request.GET.get("query", "")
        number_of_lesson = []
        courses = Course.objects.all()
        topics = Topic.objects.all()
        number_of_lesson = []

        if query:
            courses_query = Course.objects.filter(name_course__icontains=query)
            courses = courses & courses_query

        topic_filter = request.GET.get("topic", "")
        if topic_filter and topic_filter != "All":
            try:
                topic = Topic.objects.get(name_topic=topic_filter)
            except:
                topic = None
            courses_filter = Course.objects.filter(topic=topic)
            courses = courses & courses_filter

        time_learning = request.GET.get("time_learning", "")
        if time_learning == "1":
            courses_filter = Course.objects.filter(time_to_learn_ets__lte=30)
            courses = courses & courses_filter
        elif time_learning == "2":
            courses_filter = Course.objects.filter(
                time_to_learn_ets__lte=60, time_to_learn_ets__gte=30
            )
            courses = courses & courses_filter
        elif time_learning == "3":
            courses_filter = Course.objects.filter(time_to_learn_ets__gt=60)
            courses = courses & courses_filter

        level = request.GET.get("level", "")
        if level:
            courses_filter = Course.objects.filter(level=level)
            courses = courses & courses_filter

        for course in courses:
            count = len(Lesson.objects.filter(course=course))
            number_of_lesson.append(count)

        context = {"courses": zip(courses, number_of_lesson), "topics": topics}
        return render(request, self.template_name, context)
