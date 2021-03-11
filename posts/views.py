from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from .models import ArticlePost
 
# Create your views here.
class HomePageView(TemplateView): 
    template_name = 'home.html'
    
class ArticlePostListView(ListView):
    model = ArticlePost
    template_name = 'article_list.html'

class ArticlePostDetailView(DetailView):
    model = ArticlePost
    template_name = 'post_detail.html'

class ArticlePostCreateView(CreateView):
    model = ArticlePost
    template_name = 'posts/post_new.html'
    fields = ['title', 'body', 'genre']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ArticlePostUpdateView(UpdateView):
    model = ArticlePost
    template_name = 'post_edit.html'
    fields = ['title', 'body', 'genre']

class ArticlePostDeleteView(DeleteView):
    model = ArticlePost
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')

def LikeView(request, pk):
    post = get_object_or_404(ArticlePost, id=request.POST.get('articlepost.id'))
    post.likes.add(request.customuser)
    return HttpResponseRedirect(reverse('post_detail', args=[str(pk)]))