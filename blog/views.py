from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView
from django.views import generic

# Create your views here.


class PostList(ListView):
    model = Post
    template_name = "blog/post_list.html"


class DetailPostView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"

