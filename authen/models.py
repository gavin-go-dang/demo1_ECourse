from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


# Create your models here.

ROLE_CHOICES = ((1, "Student"), (2, "Teacher"))


class User(AbstractUser):
    fullname = models.CharField(max_length=50)
    date_joined = models.DateField(auto_now=True)
    date_of_birth = models.DateField(null=True, blank=True)
    type = models.CharField(max_length=9, choices=ROLE_CHOICES, default=0)
    cover_img = models.ImageField(
        upload_to=None, height_field=None, width_field=None, max_length=100
    )
