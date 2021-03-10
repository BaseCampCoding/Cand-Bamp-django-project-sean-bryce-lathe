from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.urls import reverse_lazy
from .models import Posts
# Create your views here.
class ArtistListView(LoginRequiredMixin, ListView):
    model = Posts
    template_name = 'Artist_list.html'