from django.db import models
from django.urls import reverse

# Create your models here.
class Posts(models.Model):
    title = models.CharField(max_length=200)
    author = models.foreig
    body = ...
    genre = ...