from django.db import models

from authen.models import User
from common.models import CreatedUpdatedDateModel
from .course import Course


class Certificate(CreatedUpdatedDateModel):
    student = models.ForeignKey("authen.User", on_delete=models.CASCADE)
    course = models.ForeignKey("course_manager.Course", on_delete=models.CASCADE)
    score = models.FloatField(default=0)
    pdf_url = models.URLField(null=True, blank=True)
