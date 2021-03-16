from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.views.generic import CreateView
from .forms import UserCreationForm
from .models import CustomUser
from posts.models import ArticlePost
import accounts

# Create your views here.
class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class ArtistListView(ListView):
    model = CustomUser
    template_name = 'artist_list.html'
    context_object_name = 'all_user_list'

class UserProfileDetailView(DetailView):
    model = CustomUser
    template_name = 'user_profile.html'
    # context_object_name = 'user_roles'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cur_user_id = self.request.resolver_match.kwargs["pk"]
        context['local_posts'] = ArticlePost.objects.filter(author__id=cur_user_id)
        context['roles'] = self.object.roles
        return context

    
def FollowView(request, pk):
    user_to_follow = get_object_or_404(CustomUser, id=request.user.id)
    user_to_follow.followers.add(request.user)
    user_to_follow.save()
    return HttpResponseRedirect(reverse('user_profile', args=[str(pk)]))
