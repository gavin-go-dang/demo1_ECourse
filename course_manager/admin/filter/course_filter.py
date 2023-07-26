from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from ...models import Course, Lesson


class CourseFilter(admin.SimpleListFilter):
    title = "Course"
    parameter_name = "course"

    def lookups(self, request, model_admin):
        courses = Course.objects.filter(teacher=request.user)
        return [(course.id, course.name_course) for course in courses]

    def queryset(self, request, queryset):
        pass
