from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import MentorProfile
from accounts.mixins import MentorOnlyMixin

class MentorListView(ListView):
    model = MentorProfile
    template_name = 'mentorship/mentor_list.html'
    context_object_name = 'mentors'

class MentorDetailView(DetailView):
    model = MentorProfile
    template_name = 'mentorship/mentor_detail.html'
    context_object_name = 'mentor'

def mentorship_match(request):
    # Dummy function for mentor-mentee matching logic
    mentors = MentorProfile.objects.all()
    return render(request, 'mentorship/match.html', {'mentors': mentors})

class MentorDashboardView(MentorOnlyMixin, ListView):
    model = MentorProfile
    template_name = 'mentorship/mentor_dashboard.html'
