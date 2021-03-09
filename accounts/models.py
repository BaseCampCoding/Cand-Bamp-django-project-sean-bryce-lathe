from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    ROLE_CHOICES= [
    ('listener', "Listener"),
    ('artist', "Artist")
    ]

    GENRE_CHOICES = [
        ('pop', 'Pop'),
        ('rock', 'Rock'),
        ('jazz', 'Jazz'),
        ('hip-hop', 'Hip-Hop'),
        ('blues', 'Blues'),
        ('folk', 'Folk'),
        ('country', 'Country')
    ]
    roles = models.CharField(max_length=8, choices=ROLE_CHOICES, default="Listener")
    genre = models.CharField(max_length=7, choices=GENRE_CHOICES, default="Pop")
    about = models.TextField(max_length=500)
    

# class User(AbstractUser):
#     genre =  models.CharField()
#     image = models.ImageField()
#     role = (
#         ('Listener', "Listener"),
#         ('Artist', "Artist")
#     )
#     roles = models.CharField(max_length=8,choices=role, default="Listener")
