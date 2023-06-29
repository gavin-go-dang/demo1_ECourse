from django.db import models
from .exam import Exam


class Question(models.Model):
    question_text = models.CharField(max_length=100, null=False, blank=False)
    exam = models.ForeignKey("course_manager.Exam", on_delete=models.CASCADE)
    choice_1 = models.CharField()
    choice_2 = models.CharField()
    choice_3 = models.CharField()
    choice_4 = models.CharField()
    answer = models.CharField(null=False, blank=False)

    def __str__(self):
        return self.question_text
