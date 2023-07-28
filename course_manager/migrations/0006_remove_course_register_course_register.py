# Generated by Django 4.2.2 on 2023-07-07 09:06

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("course_manager", "0005_alter_course_level"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="course",
            name="register",
        ),
        migrations.AddField(
            model_name="course",
            name="register",
            field=models.ManyToManyField(
                related_name="register", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]