from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from ...models import Course


class TimeLearningFilter(admin.SimpleListFilter):
    title = _("time to learn")
    parameter_name = "time"

    def lookups(self, request, model_admin):
        return [
            (30, _("Within 1 month")),
            (60, _("2 months")),
            (90, _("Over 3 months")),
        ]

    def queryset(self, request, queryset):
        pass
