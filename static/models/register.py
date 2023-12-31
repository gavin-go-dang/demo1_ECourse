from django.core.cache import cache
from django.db import models
from django.db.models.signals import post_save
from webpush import send_user_notification

from authen.models import User
from common.models import CreatedDateModel

from .course import Course


class Register(CreatedDateModel):
    student = models.ForeignKey("authen.User", on_delete=models.CASCADE)
    course = models.ForeignKey(
        "course_manager.Course",
        on_delete=models.CASCADE,
        related_name="course_registed",
    )

    def __str__(self):
        return "{}-{}".format(self.student, self.course)


def save_register(sender, instance, **kwargs):
    # register number on course
    course = Course.objects.get(name_course=instance.course)
    course.register += 1
    course.save()
    cache.set("top_courses", Course.objects.all().order_by("-register")[:4])

    # push notification
    payload = {
        "head": "Congrats!",
        "body": "Your register is success",
        "url": "/course/detail/{}/".format(instance.id),
    }
    send_user_notification(user=instance.student, payload=payload, ttl=1000)


post_save.connect(save_register, sender=Register)
