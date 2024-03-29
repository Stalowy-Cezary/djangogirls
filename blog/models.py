from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()

    def __str__(self):
        return self.title

class Author(models.Model):

    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)