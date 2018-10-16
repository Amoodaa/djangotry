from django.db import models
from nicelookingNewsSite.settings import MEDIA_ROOT


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.TextField(max_length=600)
    body = models.TextField(max_length=2000)
    createdAt = models.DateTimeField(auto_now=True)
    image = models.ImageField(blank=True, upload_to=MEDIA_ROOT)

    def __str__(self):
        return self.title
