from django.db import models
from authen.models import User
from .course import Course


class Lesson(models.Model):
    name_lesson = models.CharField(null=False, blank=False)
    course = models.ForeignKey(to=Course, on_delete=models.CASCADE)
    video = models.FileField()
    description = models.TextField()
    date_create = models.DateField(auto_now=True)
    view_time = models.IntegerField()

    def __str__(self):
        return self.name_lesson
