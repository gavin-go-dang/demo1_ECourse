from django.contrib import admin
from ..models import Exam, Course
from django import forms
from .filter import CourseFilter


class CourseChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return "{}".format(obj.name_course)


class ExamFilterByCourse(CourseFilter):
    def queryset(self, request, queryset):
        if self.value():
            return Exam.objects.filter(course=self.value())
        return queryset


class ExamAdmin(admin.ModelAdmin):
    list_display = ("name_exam", "course")
    fieldsets = [
        (None, {"fields": [("name_exam"), ("course")]}),
    ]
    search_fields = ("name_exam",)

    list_filter = (ExamFilterByCourse,)

    def get_queryset(self, request):
        queryset = Exam.objects.all()
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
