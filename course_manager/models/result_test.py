from django.db import models

from authen.models import User
from common.models import CreatedDateModel

from .course import Course
from .exam import Exam


class ResultTest(CreatedDateModel):
    student = models.ForeignKey("authen.User", on_delete=models.CASCADE)
    exam = models.ForeignKey("course_manager.Exam", on_delete=models.CASCADE)
    mark = models.IntegerField()
    student_answer = models.JSONField()
    number_of_test = models.IntegerField(default=1)

    def __str__(self):
        return "{}-{}".format(self.student, self.exam)
