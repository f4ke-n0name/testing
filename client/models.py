from django.db import models
import os


class ShortVideo(models.Model):
    name = models.CharField(max_length=42)
    text = models.TextField()
    content = models.FileField()

