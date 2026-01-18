from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, blank=True)
    address = models.CharField(max_length=255, blank=True)
    bio = models.TextField(blank=True)
    profile_pic = models.ImageField(
        default='default.jpg',
        upload_to='profile_pic/',
        blank=True,
        null=True
    )

    def __str__(self):
        return f"{self.user.username} Profile"
