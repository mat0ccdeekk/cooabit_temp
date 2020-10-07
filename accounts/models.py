from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image
from social_site import settings
# Create your models here.


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    city = models.CharField(max_length=50, null=True)
    occupation = models.CharField(max_length=50, null=True)
    age = models.DateField(blank=True, null=True, default="")
    gender = models.CharField(max_length=10, null=True)

    state = models.CharField(max_length=50, blank=True, null=True)

    mobile = models.CharField(max_length=50, blank=True, null=True, default=" ")
    photo = models.ImageField(upload_to="profile/", default='profile/superman.jpeg', blank=True, null=True)
    aboutMe = models.CharField(max_length=500, blank=True, null=True, default="Su di me..")
    maxima = models.CharField(max_length=50, blank=True, null=True)
    pet = models.CharField(max_length=1, blank=True, null=True)
    owner = models.CharField(max_length=10, blank=True, null=True, default="profile")
    
    idZoom1 = models.CharField(max_length=300, blank=True, null=True, default="zero")
    idZoom2 = models.CharField(max_length=300, blank=True, null=True, default="zero")
    link1 = models.CharField(max_length=300, blank=True, null=True, default="zero")
    link2 = models.CharField(max_length=300, blank=True, null=True, default="zero")
    pass1 = models.CharField(max_length=300, blank=True, null=True, default="zero")
    pass2 = models.CharField(max_length=300, blank=True, null=True, default="zero")


    def __str__(self):
        return self.user.email
    #
    # def save(self):
    #     super().save()
    #     print("percorsoooooo",self.photo.path)
    #     img = Image.open(self.photo.path)
    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.photo.path)

class ProfileP(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    mobile = models.CharField(max_length=50, blank=True, null=True, default="n")
    agency = models.CharField(max_length=50, blank=True, null=True, default="n")
    owner = models.CharField(max_length=10, blank=True, null=True, default="profilep")


    def __str__(self):
        return self.user.email
