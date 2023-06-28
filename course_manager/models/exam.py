from django.db import models
from .course import Course


class Exam(models.Model):
    name_exam = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField()
    date_create = models.DateField(auto_now=True)

    def __str__(self):
        return self.name_exam
