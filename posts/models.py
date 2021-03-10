from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
# Create your models here.
GENRE_CHOICES = [
        ('pop', 'Pop'),
        ('rock', 'Rock'),
        ('jazz', 'Jazz'),
        ('hip-hop', 'Hip-Hop'),
        ('blues', 'Blues'),
        ('folk', 'Folk'),
        ('country', 'Country')
    ]
class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    body = models.TextField()
    genre = models.CharField(max_length=7, choices=GENRE_CHOICES, default="Pop")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])