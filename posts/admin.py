from django.contrib import admin
from .models import ArticlePost, Comment, Song
# Register your models here.

admin.site.register(ArticlePost)
admin.site.register(Comment)
admin.site.register(Song)