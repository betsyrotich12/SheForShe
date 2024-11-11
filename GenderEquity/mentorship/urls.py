from django.urls import path
from . import views

urlpatterns = [
    path('', views.MentorListView.as_view(), name='mentor_list'),
    path('profile/<int:pk>/', views.MentorDetailView.as_view(), name='mentor_profile'),
    path('match/', views.mentorship_match, name='mentor_match'),
]
