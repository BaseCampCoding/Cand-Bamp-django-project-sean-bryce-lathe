from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import UserCreationForm
from .models import CustomUser

# Create your views here.
class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class ArtistListView(LoginRequiredMixin, ListView):
    model = CustomUser
    template_name = 'Artist_list.html'
    context_object_name = 'all_user_list'