from django.urls import path
from .views import (PostCreateView, PostDeleteView, PostDetailView, PostListView, PostUpdateView,)

urlpatterns = [
    path('post/<int:pk>/edit', PostUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post_delete'),
    path('', PostListView.as_view(), name='Article_list'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('post/new', PostCreateView.as_view(), name='post_new'),
]
