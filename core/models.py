from django.db import models

# Create your models here.

class subscription(models.Model):
    nome = models.CharField(max_length=40)
    cognome = models.CharField(max_length=40)
    email = models.CharField(max_length=40)

    def __str__(self):
        return self.email
