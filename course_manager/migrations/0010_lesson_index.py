# Generated by Django 4.2.2 on 2023-07-24 09:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("course_manager", "0009_merge_0006_alter_course_teacher_0008_register"),
    ]

    operations = [
        migrations.AddField(
            model_name="lesson",
            name="index",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
