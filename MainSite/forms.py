from django.forms import *
from django.db import models
from django.conf.global_settings import MEDIA_ROOT


class Form1:
    title = models.CharField(max_length=255)
    subtitle = models.TextField(max_length=600)
    body = models.TextField(max_length=2000)
    createdAt = models.DateTimeField(auto_now=True)
    image = models.ImageField(blank=True, upload_to=MEDIA_ROOT)
