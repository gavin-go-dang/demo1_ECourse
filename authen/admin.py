from django.contrib import admin

from .models import User

# Register your models here.


class TeacherAdmin(admin.ModelAdmin):
    list_display = ("full_name", "date_of_birth", "type")
    fieldsets = [
        (
            None,
            {
                "fields": [
                    ("full_name"),
                    ("date_of_birth"),
                    ("cover_img"),
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
            return queryset.filter(id=teacher.id)


admin.site.register(User, TeacherAdmin)
