from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import ForumPost

class ForumListView(ListView):
    model = ForumPost
    template_name = 'forum/forum_list.html'
    context_object_name = 'posts'

class ForumDetailView(DetailView):
    model = ForumPost
    template_name = 'forum/forum_detail.html'
    context_object_name = 'post'

class ForumCreateView(CreateView):
    model = ForumPost
    template_name = 'forum/create_post.html'
    fields = ['title', 'content']
    success_url = '/forum/'

