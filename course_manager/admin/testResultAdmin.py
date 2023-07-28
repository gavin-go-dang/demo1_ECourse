from django.contrib import admin

from course_manager.models import ResultTest


class ResultTestAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "student",
        "exam",
        "number_of_test",
    )

    fieldsets = [
        (
            None,
            {
                "fields": [
                    ("student"),
                    ("exam"),
                    ("mark"),
                    ("student_answer"),
                    ("number_of_test"),
                ]
            },
        ),
    ]

    def get_queryset(self, request):
        queryset = super().get_queryset(request)

        if request.user.is_superuser:
            return queryset
        else:
            teacher = request.user
            return queryset.filter(exam__course__teacher=teacher)
