from django.db import models
from .course import Course
from common.models import BaseModel


class Exam(BaseModel):
    name_exam = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField()

    def __str__(self):
        return self.name_exam
