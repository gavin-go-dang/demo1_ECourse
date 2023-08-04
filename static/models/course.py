from django.db import models

from authen.models import User
from common.models import CreatedUpdatedDateModel

from .topic import Topic


class Course(CreatedUpdatedDateModel):
    LEVEL_CHOICES = (("basic", "Basic"), ("medium", "Medium"), ("advanced", "Advanced"))
    name_course = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField()
    topic = models.ForeignKey(
        "course_manager.Topic", on_delete=models.SET_NULL, null=True, blank=True
    )
    teacher = models.ForeignKey(
        "authen.User", on_delete=models.CASCADE, null=True, blank=True
    )
    register = models.IntegerField(default=0)
    time_to_learn_ets = models.IntegerField(default=0)
    cover_img = models.ImageField(upload_to="course_img/", null=True, blank=True)
    level = models.CharField(choices=LEVEL_CHOICES, blank=True, null=True)

    def __str__(self):
        return self.name_course
