from django.db import models
from django.utils.timezone import now

# Create your models here.


class BaseModel(models.Model):
    created_at = models.DateField(
        verbose_name="Created At", default=now, editable=False
    )
    updated_at = models.DateField(verbose_name="Updated At", default=now)

    class Meta:
        abstract = True

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        if not self.id:
            self.updated_at = now()
            return super().save(force_insert, force_update, using, update_fields)
