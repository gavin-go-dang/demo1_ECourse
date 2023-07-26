from django.contrib import admin
from ..models import Lesson, Course
from django import forms
from .filter import CourseFilter


class CourseChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return "{}".format(obj.name_course)


class LessonFilterByCourse(CourseFilter):
    def queryset(self, request, queryset):
        if self.value():
            return Lesson.objects.filter(course=self.value())
        return queryset


class LessonAdmin(admin.ModelAdmin):
    list_display = ("name_lesson", "course", "view_time")

    fieldsets = [
        (
            None,
            {
                "fields": [
                    ("name_lesson"),
                    ("course"),
                    ("video"),
                    ("description"),
                    ("index"),
                    ("view_time"),
                ]
            },
        ),
    ]

    list_filter = (LessonFilterByCourse,)

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if request.user.is_superuser:
            return queryset
        else:
            teacher = request.user
            return queryset.filter(course__teacher=teacher)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "course":
            return CourseChoiceField(
                queryset=Course.objects.filter(teacher=request.user)
            )
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
