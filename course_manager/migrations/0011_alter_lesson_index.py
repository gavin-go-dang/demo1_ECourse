# Generated by Django 4.2.2 on 2023-07-24 09:49

import builtins

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("course_manager", "0010_lesson_index"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lesson",
            name="index",
            field=models.IntegerField(blank=True, default=builtins.id, null=True),
        ),
    ]
