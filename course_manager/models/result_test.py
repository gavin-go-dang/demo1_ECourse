from django.db import models
from .course import Course
from authen.models import User
from .exam import Exam


class ResultTest(models.Model):
    student = models.ForeignKey(to=User, on_delete=models.CASCADE)
    exam = models.ForeignKey(to=Exam, on_delete=models.CASCADE)
    mark = models.IntegerField()
    date_test = models.DateField(auto_now=True)
    student_answer = models.JSONField()
    number_of_test = models.IntegerField(default=1)

    def __str__(self):
        return "-".format(self.student, self.exam)
