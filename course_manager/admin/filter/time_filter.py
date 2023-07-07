from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from ...models import Course


class TimeLearningFilter(admin.SimpleListFilter):
    title = _("Filter by time to learn")
    parameter_name = "time"

    def lookups(self, request, model_admin):
        return [
            (1, _("Within 1 month")),
            (2, _("Within 2 months")),
            (3, _("Over 3 months")),
        ]

    def queryset(self, request, queryset):
        if self.value() == 1:
            return Course.objects.filter(time_to_learn_ets__lte=30)
        elif self.value() == 2:
            return Course.objects.filter(time_to_learn_ets__lte=60)
        else:
            return Course.objects.filter(time_to_learn_ets__gt=60)
