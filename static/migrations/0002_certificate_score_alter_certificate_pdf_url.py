# Generated by Django 4.2.2 on 2023-07-31 02:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("course_manager", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="certificate",
            name="score",
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name="certificate",
            name="pdf_url",
            field=models.URLField(blank=True, null=True),
        ),
    ]
