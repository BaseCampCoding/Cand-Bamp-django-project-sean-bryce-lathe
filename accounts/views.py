from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.views.generic import CreateView
from .forms import UserCreationForm
from .models import CustomUser
import accounts

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

def FollowView(request, pk):
    follow = get_object_or_404(CustomUser, id=request.POST.get('to_customuser_id'))
    accounts.followers.add(request.user)
    return HttpResponseRedirect(reverse('user_profile', args=[str(pk)]))