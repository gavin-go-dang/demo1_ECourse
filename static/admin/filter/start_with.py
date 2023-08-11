from django.contrib import admin
from django.db.models.functions import Substr


class FirstLetterFilter(admin.SimpleListFilter):
    title = "First Letter"
    parameter_name = "first_letter"
    field_filter = None

    def lookups(self, request, model_admin):
        queryset = model_admin.get_queryset(request)
        first_letters = (
            queryset.annotate(first_letter=Substr(self.field_filter, 1, 1))
            .values_list("first_letter", flat=True)
            .distinct()
        )
        return [(letter, letter.upper()) for letter in first_letters]

    def queryset(self, request, queryset):
        return
