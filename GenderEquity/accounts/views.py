# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserProfileForm
from django.contrib.auth.decorators import user_passes_test

@login_required
def profile_view(request):
    profile = request.user.userprofile
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to the profile view
    else:
        form = UserProfileForm(instance=profile)
    return render(request, 'accounts/profile.html', {'form': form})

def is_mentor(user):
    return user.userprofile.role == 'Mentor' or user.userprofile.role == 'Moderator'

@user_passes_test(is_mentor)
def mentor_dashboard(request):
    return render(request, 'accounts/mentor_dashboard.html')

def is_mentee(user):
    return user.userprofile.role == 'Mentee'

@user_passes_test(is_mentee)
def mentee_dashboard(request):
    return render(request, 'accounts/mentee_dashboard.html')

