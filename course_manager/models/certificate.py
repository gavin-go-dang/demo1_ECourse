from django.db import models
from authen.models import User
from .course import Course


class Certificate(models.Model):
    student = models.ForeignKey("authen.User", on_delete=models.CASCADE)
    course = models.ForeignKey("course_manager.Course", on_delete=models.CASCADE)
    pdf_url = models.URLField()
