from django.db import models

from authen.models import User
from common.models import CreatedDateModel
from django.db.models.signals import post_save
from .course import Course
from .exam import Exam
from webpush import send_user_notification


class ResultTest(CreatedDateModel):
    student = models.ForeignKey("authen.User", on_delete=models.CASCADE)
    exam = models.ForeignKey("course_manager.Exam", on_delete=models.CASCADE)
    mark = models.IntegerField()
    student_answer = models.JSONField()
    number_of_test = models.IntegerField(default=1)
    pass_exam = models.BooleanField(default=False)

    def __str__(self):
        return "{}-{}".format(self.student, self.exam)


def save_register(sender, instance, **kwargs):
    # push notification
    pass_score = 7.5
    if instance.mark > pass_score:
        payload = {
            "head": "Congrats!",
            "body": "Congratulations! You have passed the exam",
            "url": "/study/result/",
        }
        send_user_notification(user=instance.student, payload=payload, ttl=1000)

    else:
        payload = {
            "head": "Please re-do this exam",
            "url": "/study/result/",
        }
        send_user_notification(user=instance.student, payload=payload, ttl=1000)


post_save.connect(save_register, sender=ResultTest)
