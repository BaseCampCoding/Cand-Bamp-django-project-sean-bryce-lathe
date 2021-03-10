from django.urls import path
from .views import (ArtistListView, PostCreateView, PostDeleteView, PostDetailView, PostListView, PostUpdateView,)

urlpatterns = [
    path('post/<int:pk>/edit', PostUpdateView.as_view(), name='post_edit'),
    path('post/new', PostCreateView.as_view(), name='post_new'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post_delete'),
    # path('', PostListView.as_view(), name='Artist_list'),
    path('', ArtistListView.as_view(), name='artist_list'),
]
