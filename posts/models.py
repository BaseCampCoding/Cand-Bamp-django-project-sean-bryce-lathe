from django.db import models
from django.urls import reverse, reverse_lazy
from django.contrib.auth import get_user_model
from accounts.models import CustomUser

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
class ArticlePost(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    body = models.TextField()
    genre = models.CharField(max_length=7, choices=GENRE_CHOICES, default="Pop")
    likes = models.ManyToManyField(CustomUser, related_name="user_article_post_likes")
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

    def total_likes(self):
        return self.likes.count()


class Song(models.Model):
    title = models.TextField()
    artist = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    image = models.ImageField(upload_to="song_image", blank=True)
    audio_file = models.FileField(upload_to="song_file", blank=True, null=True)
    duration = models.CharField(max_length=20)
    paginate_by = 2

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(ArticlePost, related_name="comments", on_delete=models.CASCADE,)
    name = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    body = models.TextField()
    data_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)
    def get_absolute_url(self):
        return reverse_lazy('article_list', args=[str(self.id)])