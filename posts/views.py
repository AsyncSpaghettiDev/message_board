from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post


class HomeView(TemplateView):
    template_name = 'posts/home.html'


class AboutView(TemplateView):
    template_name = 'posts/about.html'


class PostListView(ListView):
    template_name = "posts/list.html"
    model = Post


class PostDetailView(DetailView):
    template_name = "posts/detail.html"
    model = Post


class PostCreateView(CreateView):
    template_name = "posts/create.html"
    model = Post
    fields = ["title", "subtitle", "body"]
