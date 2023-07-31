from django import forms
from django.contrib import admin

from ..models import Course, Exam, Lesson, Question


class ExamChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return "{} - {}".format(obj.name_exam, obj.course.name_course)


class QuestionAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "exam",
        "question_text",
        "answer",
    )

    fieldsets = [
        (
            None,
            {
                "fields": [
                    ("question_text"),
                    ("exam"),
                    ("choice_1"),
                    ("choice_2"),
                    ("choice_3"),
                    ("choice_4"),
                    ("answer"),
                ]
            },
        ),
    ]

    list_filter = ("exam",)

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if request.user.is_superuser:
            return queryset
        else:
            teacher = request.user
            return queryset.filter(exam__course__teacher=teacher)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "exam":
            return ExamChoiceField(
                queryset=Exam.objects.filter(course__teacher=request.user)
            )
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
