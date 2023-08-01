from django.db import models

from authen.models import User
from common.models import CreatedUpdatedDateModel
from django.db.models.signals import post_save

from .lesson import Lesson


class LessonLearned(CreatedUpdatedDateModel):
    student = models.ForeignKey("authen.User", on_delete=models.CASCADE)
    lesson = models.ForeignKey("course_manager.Lesson", on_delete=models.CASCADE)


def save_lesson_learned(sender, instance, **kwargs):
    # push notification
    payload = {"head": "Congrats!", "body": "Your register is success"}
    send_user_notification(user=instance.student, payload=payload, ttl=1000)


post_save.connect(save_lesson_learned, sender=LessonLearned)
