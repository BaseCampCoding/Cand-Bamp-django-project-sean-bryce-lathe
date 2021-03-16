from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from .models import ArticlePost, Comment, Song
from .forms import CommentForm

 
# Create your views here.
class HomePageView(TemplateView): 
    template_name = 'home.html'
    
class ArticlePostListView(ListView):
    model = ArticlePost
    template_name = 'article_list.html'

class ArticlePostCreateView(LoginRequiredMixin, CreateView):
    model = ArticlePost
    template_name = 'post_new.html'
    fields = ['title', 'body', 'genre']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ArticlePostDetailView(DetailView):
    model = ArticlePost
    template_name = 'post_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        TFLC = get_object_or_404(ArticlePost, id=self.kwargs['pk'])
        liked = False
        if TFLC.likes.filter(id=self.request.user.id).exists():
            liked = True
        total_likes = TFLC.total_likes()
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context

# class ArticlePostCreateView(LoginRequiredMixin, CreateView):
#     model = ArticlePost
#     template_name = 'posts/post_new.html'
#     fields = ['title', 'body', 'genre']
    
class SongPostCreateView(CreateView):
    model = Song
    success_url = reverse_lazy('artist_list')
    template_name = 'posts/song_new.html'
    fields = ['title', 'image', 'audio_file', 'duration']

    def form_valid(self, form):
        form.instance.artist = self.request.user
        return super().form_valid(form)

class SongPostDetailView(DetailView):
    model = Song
    template_name = 'artist_song.html'

class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'add_comment.html'
    
    def form_valid(self, form):
        form.instance.name = self.request.user
        temp_id = self.request.resolver_match.kwargs["pk"]
        temp_obj = ArticlePost.objects.get(id=temp_id)
        form.instance.post = temp_obj
        return super().form_valid(form)
    success_url = reverse_lazy('article_list')

class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    template_name = 'comment_edit.html'
    form_class = CommentForm
    success_url = reverse_lazy('article_list')

    def test_func(self): 
        obj = self.get_object()
        return obj.name == self.request.user

class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'comment_delete.html'
    success_url = reverse_lazy('article_list')

    def test_func(self): 
        obj = self.get_object()
        return obj.name == self.request.user

class ArticlePostUpdateView(UpdateView):
    model = ArticlePost
    template_name = 'post_edit.html'
    fields = ['title', 'body', 'genre']
    
class ArticlePostDeleteView(DeleteView):
    model = ArticlePost
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')

def LikeView(request, pk):
    post = get_object_or_404(ArticlePost, id=request.POST.get('articlepost_id'))
    post.likes.add(request.user)
    # return HttpResponseRedirect(reverse('post_detail', args=[str(pk)]))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('post_detail', args=[str(pk)]))
    

class HomeDetailPage(DetailView):
    model = ArticlePost
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['detail_posts'] = ArticlePost.objects.all()
        return context