from django.urls import path
from . import views

urlpatterns = [
    path('', views.StoryListView.as_view(), name='story_list'),
    path('story/<int:pk>/', views.StoryDetailView.as_view(), name='story_detail'),
    path('submit/', views.StoryCreateView.as_view(), name='submit_story'),
]
