from django.contrib import admin

from ..models import Course
from .filter import FirstLetterFilter, TimeLearningFilter


class FirstLetterCourseFilter(FirstLetterFilter):
    field_filter = "name_course"

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(name_course__istartswith=self.value())
        return queryset


class FilterByTimeToLearn(TimeLearningFilter):
    def queryset(self, request, queryset):
        courses = Course.objects.filter(teacher=request.user)
        if self.value():
            return courses.filter(time_to_learn_ets__lte=self.value()).filter(
                time_to_learn_ets__gt=int(self.value()) - 30
            )
        return queryset


class CourseAdmin(admin.ModelAdmin):
    list_display = (
        "name_course",
        "topic",
        "register",
        "teacher",
        "time_to_learn_ets",
        "level",
    )
    fieldsets = [
        (
            None,
            {
                "fields": [
                    ("name_course"),
                    ("description"),
                    ("topic"),
                    ("time_to_learn_ets"),
                    ("cover_img"),
                    ("level"),
                ]
            },
        ),
    ]
    search_fields = ("name_course",)
    list_filter = (
        FirstLetterCourseFilter,
        "topic",
        "level",
        FilterByTimeToLearn,
    )

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if request.user.is_superuser:
            return queryset
        else:
            teacher = request.user
            return queryset.filter(teacher=teacher)

    def save_model(self, request, obj, form, change):
        if getattr(obj, "teacher", None) is None:
            obj.teacher = request.user
        obj.save()
