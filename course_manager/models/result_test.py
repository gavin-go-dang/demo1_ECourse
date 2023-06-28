from django.db import models
from .course import Course
from authen.models import User
from .exam import Exam
from common.models import BaseModel


class ResultTest(BaseModel):
    student = models.ForeignKey(to=User, on_delete=models.CASCADE)
    exam = models.ForeignKey(to=Exam, on_delete=models.CASCADE)
    mark = models.IntegerField()
    student_answer = models.JSONField()
    number_of_test = models.IntegerField(default=1)

    def __str__(self):
        return "-".format(self.student, self.exam)
