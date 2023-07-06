from django.contrib import admin
from ..models import Lesson


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
                    ("view_time"),
                ]
            },
        ),
    ]

    def get_queryset(self, request):
        queryset = Lesson.objects.all()
        if request.user.is_superuser:
            return queryset
        else:
            teacher = request.user
            return queryset.filter(course__teacher=teacher)
