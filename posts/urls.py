from django.urls import path
from .views import (PostCreateView, PostDeleteView, PostDetailView, PostListView, PostUpdateView, HomePageView,)

urlpatterns = [
    path('post/<int:pk>/edit', ArticlePostUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete', ArticlePostDeleteView.as_view(), name='post_delete'),
    path('post/', ArticlePostListView.as_view(), name='article_list'),
    path('post/<int:pk>', ArticlePostDetailView.as_view(), name='post_detail'),
    path('post/new', ArticlePostCreateView.as_view(), name='post_new'),
    path('', HomePageView.as_view(), name='home'),
]
