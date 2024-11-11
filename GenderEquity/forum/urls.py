from django.urls import path
from . import views

urlpatterns = [
    path('', views.ForumListView.as_view(), name='forum_list'),
    path('post/<int:pk>/', views.ForumDetailView.as_view(), name='forum_post'),
    path('create/', views.ForumCreateView.as_view(), name='create_forum_post'),
]
