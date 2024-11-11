# accounts/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile_view, name='profile'),  # Profile page (profile management)
    path('mentor-dashboard/', views.mentor_dashboard, name='mentor_dashboard'),  # Mentor-specific page
    path('mentee-dashboard/', views.mentee_dashboard, name='mentee_dashboard'),  # Mentee-specific page
]
