from django.db import models


class Text(models.Model):
    content = models.TextField()
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    language = models.CharField(max_length=50)
    cover = models.CharField(null=True, blank=True)
    pages = models.IntegerField(null=True, blank=True)
