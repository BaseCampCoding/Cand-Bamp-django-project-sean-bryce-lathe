from django.urls import path
from .views import SignUpView, ArtistListView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('', ArtistListView.as_view(), name='artist_list'),
]