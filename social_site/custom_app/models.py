from django.db import models

# Create your models here.



class zoom(models.Model):

    user = models.CharField(max_length=50, null=True, blank=True, default="zero")
    conferma = models.CharField(max_length=50, null=True, blank=True, default="zero")
    casa = models.CharField(max_length=50, null=True, blank=True, default="home0")


    def __str__(self):
        return self.user+" "+self.conferma
