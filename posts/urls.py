from django.urls import path

from .views import (
    ArticlePostCreateView, 
    ArticlePostDeleteView, 
    ArticlePostDetailView,
    ArticlePostListView,
    ArticlePostUpdateView,
    SongPostCreateView,
    SongPostDetailView,
    HomePageView,
    AddCommentView,
    CommentDeleteView,
    CommentUpdateView,
    LikeView,
)

urlpatterns = [
    path('song/', SongPostDetailView.as_view(), name='artist_song'),
    path('song/new', SongPostCreateView.as_view(), name='song_new'),
    path('post/<int:pk>/edit', ArticlePostUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete', ArticlePostDeleteView.as_view(), name='post_delete'),
    path('post/', ArticlePostListView.as_view(), name='article_list'),
    path('post/<int:pk>/detail', ArticlePostDetailView.as_view(), name='post_detail'),
    path('post/new', ArticlePostCreateView.as_view(), name='post_new'),
    path('', HomePageView.as_view(), name='home'),
    path('post/<int:pk>/comment', AddCommentView.as_view(), name='add_comment'),
    path('post/<int:pk>/comment/delete', CommentDeleteView.as_view(), name='comment_delete'),
    path('post/<int:pk>/comment/edit', CommentUpdateView.as_view(), name='comment_edit'),
    path('like/<int:pk>', LikeView, name="like_articlepost"),
]
