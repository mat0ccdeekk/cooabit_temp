from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image
from social_site import settings
from datetime import date
# Create your models here.


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    city = models.CharField(max_length=50, null=True)
    occupation = models.CharField(max_length=50, null=True)
    age = models.DateField(default=date.today)
    gender = models.CharField(max_length=10, null=True)
    mobile = models.CharField(max_length=50, blank=True, null=True, default=" ")
    photo = models.ImageField(upload_to="profile/", default='profile/superman.jpeg', blank=True, null=True)
    owner = models.CharField(max_length=10, blank=True, null=True, default="profile")


    def __str__(self):
        return self.user.email

class ProfileStatus(models.Model):
    user_profile    = models.ForeignKey(Profile, on_delete=models.CASCADE)
    status_content  = models.CharField(max_length=255)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "statuses"

    def __str__(self):
        return str(self.user_profile)

class ProfileP(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    mobile = models.CharField(max_length=50, blank=True, null=True, default="n")
    agency = models.CharField(max_length=50, blank=True, null=True, default="n")
    owner = models.CharField(max_length=10, blank=True, null=True, default="profilep")


    def __str__(self):
        return self.user.email
