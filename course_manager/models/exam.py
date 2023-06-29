from django.db import models
from .course import Course
from common.models import CreatedUpdatedDateModel
from .course import Course


class Exam(CreatedUpdatedDateModel):
    name_exam = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField()
    course = models.ForeignKey("course_manager.Course", on_delete=models.CASCADE)

    def __str__(self):
        return self.name_exam
