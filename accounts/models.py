from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models

ROLE_CHOICES= [
    ('listener', 'Listener'),
    ('artist', 'Artist'),
]
# Create your models here.
class User(AbstractUser):
    image = models.ImageField()
    roles = forms.CharField(label='What role would you like to be?', widget=forms.Select(choices=ROLE_CHOICES) default="Listener")
    fav_genre = models.CharField(max_length=200)
    about = models.TextField(max_length=500)
    
# Create your models here.
# class User(AbstractUser):
#     genre =  models.CharField()
#     image = models.ImageField()
#     role = (
#         ('Listener', "Listener"),
#         ('Artist', "Artist")
#     )
#     roles = models.CharField(max_length=8,choices=role, default="Listener")
