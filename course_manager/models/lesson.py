from django.db import models

from authen.models import User
from common.models import CreatedUpdatedDateModel

from .course import Course


class Lesson(CreatedUpdatedDateModel):
    name_lesson = models.CharField(null=False, blank=False)
    course = models.ForeignKey(
        "course_manager.Course", on_delete=models.CASCADE, related_name="course"
    )
    video = models.FileField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    view_time = models.IntegerField(null=True, blank=True)
    index = models.IntegerField(null=True, blank=True, default=id)

    def __str__(self):
        return self.name_lesson
