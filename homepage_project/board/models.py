
from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):        
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=50)
    text = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)
    tag = models.CharField(max_length=1000)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
