from django.db import models
from django.db.models.signals import post_save
from webpush import send_user_notification

from authen.models import User
from common.models import CreatedUpdatedDateModel

from .lesson import Lesson


class LessonLearned(CreatedUpdatedDateModel):
    student = models.ForeignKey("authen.User", on_delete=models.CASCADE)
    lesson = models.ForeignKey("course_manager.Lesson", on_delete=models.CASCADE)


def save_lesson_learned(sender, instance, **kwargs):
    payload = {
        "head": "Congrats!",
        "body": "Congratulations! You have completed {} lesson".format(instance.lesson),
        "icon": "https://i.ibb.co/MDVY8w2/success-image.png",
        "url": "/study/lesson/{}/".format(instance.lesson.id),
    }
    send_user_notification(user=instance.student, payload=payload, ttl=1000)


post_save.connect(save_lesson_learned, sender=LessonLearned)
