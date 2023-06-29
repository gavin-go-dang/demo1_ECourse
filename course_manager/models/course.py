from django.db import models
from authen.models import User
from .topic import Topic
from common.models import CreatedUpdatedDateModel


class Course(CreatedUpdatedDateModel):
    name_course = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField()
    topic = models.ForeignKey(
        "course_manager.Topic", on_delete=models.SET_NULL, null=True, blank=True
    )
    teacher = models.ForeignKey("authen.User", on_delete=models.CASCADE)
    register = models.IntegerField(default=0)

    def __str__(self):
        return self.name_course
