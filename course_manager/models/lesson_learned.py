from django.db import models
from .lesson import Lesson
from authen.models import User
from common.models import CreatedUpdatedDateModel


class LessonLearned(CreatedUpdatedDateModel):
    student = models.ForeignKey("authen.User", on_delete=models.CASCADE)
    lesson = models.ForeignKey("course_manager.Lesson", on_delete=models.CASCADE)
