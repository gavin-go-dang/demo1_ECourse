from django.db import models
from authen.models import User
from .course import Course


class Certificate(models.Model):
    student = models.ForeignKey(to=User, on_delete=models.CASCADE)
    course = models.ForeignKey(to=Course, on_delete=models.CASCADE)
    pdf_url = models.URLField()
