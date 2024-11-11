from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class MentorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    expertise = models.TextField()
    location = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return self.user.username
