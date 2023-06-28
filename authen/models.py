from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from common.models import BaseModel


# Create your models here.


class User(AbstractUser, BaseModel):
    ROLE_CHOICES = (("student", "Student"), ("teacher", "Teacher"))
    full_name = models.CharField(max_length=50)
    date_of_birth = models.DateField(null=True, blank=True)
    type = models.CharField(choices=ROLE_CHOICES)
    cover_img = models.ImageField(
        upload_to="cover_img/", height_field=None, width_field=None, max_length=100
    )
