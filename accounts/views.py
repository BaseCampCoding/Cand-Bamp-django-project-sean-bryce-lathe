from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import UserCreationForm
from .models import CustomUser
from posts.models import ArticlePost

# Create your views here.
class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class ArtistListView(LoginRequiredMixin, ListView):
    model = CustomUser
    template_name = 'artist_list.html'
    context_object_name = 'all_user_list'

class UserProfileDetailView(DetailView):
    model = CustomUser
    template_name = 'user_profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cur_user_id = self.request.resolver_match.kwargs["pk"]
        context['local_posts'] = ArticlePost.objects.filter(author__id=cur_user_id)
        return context