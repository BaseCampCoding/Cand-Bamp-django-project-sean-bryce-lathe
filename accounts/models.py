from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from django import forms

ROLE_CHOICES= [
    ('listener', 'Listener'),
    ('artist', 'Artist'),
]

GENRE_CHOICES = [
    ('Rock', 'rock'),
    ('Jazz', 'jazz'),
    ('hip-hop', 'Hip-Hop'),
    ('Blues', 'blues'),
    ('Folk', 'folk'),
    ('Country', 'country'),
    ('Pop', 'pop'),
]

# Create your models here.
class User(AbstractUser):
    image = models.ImageField()
    roles = forms.CharField(label='What role would you like to be?', widget=forms.Select(choices=ROLE_CHOICES), default="Listener")
    genre = models.CharField(label="What is your favorite genre?", widget=forms.Select(choices=GENRE_CHOICES), null=True)
    about = models.TextField(max_length=500)
    

# class User(AbstractUser):
#     genre =  models.CharField()
#     image = models.ImageField()
#     role = (
#         ('Listener', "Listener"),
#         ('Artist', "Artist")
#     )
#     roles = models.CharField(max_length=8,choices=role, default="Listener")
