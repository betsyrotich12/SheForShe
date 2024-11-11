
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import redirect

class MentorOnlyMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.userprofile.role == 'Mentor' or self.request.user.userprofile.role == 'Moderator'

    def handle_no_permission(self):
        return redirect('no_permission')  # Redirect to a "No Permission" page or show an error
