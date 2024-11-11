from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=100, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])
    interests = models.TextField(help_text="Interests in education, GBV, FGM, mentorship")
    role = models.CharField(
        max_length=10,
        choices=[('Mentor', 'Mentor'), ('Mentee', 'Mentee'), ('Moderator', 'Moderator')],
        default='Mentee'
    )

    def __str__(self):
        return f"{self.user.username}'s profile"

