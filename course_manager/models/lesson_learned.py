from django.db import models
from .lesson import Lesson
from authen.models import User


class LessonLearned(models.Model):
    student = models.ForeignKey(to=User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(to=Lesson, on_delete=models.CASCADE)
