from django.contrib import admin
from ..models import Exam


class ExamAdmin(admin.ModelAdmin):
    list_display = ("name_exam", "course")
    fieldsets = [
        (None, {"fields": [("name_exam"), ("course")]}),
    ]
    search_fields = ("name_exam",)

    def get_queryset(self, request):
        queryset = Exam.objects.all()
        if request.user.is_superuser:
            return queryset
        else:
            teacher = request.user
            return queryset.filter(course__teacher=teacher)
