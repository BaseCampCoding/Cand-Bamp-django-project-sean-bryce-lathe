from django.urls import path
from .views import SignUpView, ArtistListView, UserProfileDetailView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('user/<int:pk>', UserProfileDetailView.as_view(), name='user_profile'),
    path('', ArtistListView.as_view(), name='artist_list'),
]