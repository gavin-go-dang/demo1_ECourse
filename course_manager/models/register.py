from django.db import models
from authen.models import User
from .course import Course
from common.models import CreatedDateModel
from django.db.models.signals import post_save
from django.core.cache import cache


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
    course = Course.objects.get(name_course=instance.course)
    course.register += 1
    course.save()
    cache.set("top_courses", Course.objects.all().order_by("-register")[:4])


post_save.connect(save_register, sender=Register)
