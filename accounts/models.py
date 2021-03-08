from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models

ROLE_CHOICES= [
    ('listener', 'Listener'),
    ('artist', 'Artist'),
]
# Create your models here.
class User(AbstractUser):
    roles = forms.CharField(label='What role would you like to be?', widget=forms.Select(choices=ROLE_CHOICES))
    fav_genre = models.CharField(max_length=200)
    about = = models.TextField(max_length=500)
    