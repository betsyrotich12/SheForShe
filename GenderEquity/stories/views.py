from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Story

class StoryListView(ListView):
    model = Story
    template_name = 'stories/story_list.html'
    context_object_name = 'stories'

class StoryDetailView(DetailView):
    model = Story
    template_name = 'stories/story_detail.html'
    context_object_name = 'story'

class StoryCreateView(CreateView):
    model = Story
    template_name = 'stories/submit_story.html'
    fields = ['title', 'content', 'author']
    success_url = '/stories/'

