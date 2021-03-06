from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.apps import apps
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
    profile_picture = models.ImageField(upload_to="profile_image", blank=True)
    genre = models.CharField(max_length=7, choices=GENRE_CHOICES, default="Pop")
    about = models.TextField(max_length=500)
    
    followers = models.ManyToManyField("self", symmetrical=False, blank=True, related_name="m_followers")
    def total_likes(self):
        Posts = apps.get_model("posts", "ArticlePost")
        all_posts_by_user = Posts.objects.filter(author__id=self.id)
        total = 0
        for i in all_posts_by_user:
            total += i.total_likes()
        return total
    
    def total_follower(self):
        return self.followers.count()

# class User(AbstractUser):
#     genre =  models.CharField()
#     image = models.ImageField()
#     role = (
#         ('Listener', "Listener"),
#         ('Artist', "Artist")
#     )
#     roles = models.CharField(max_length=8,choices=role, default="Listener")
