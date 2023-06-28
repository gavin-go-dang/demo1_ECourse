from django.db import models


class Topic(models.Model):
    name_topic = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField()

    def __str__(self):
        return self.topic_name
