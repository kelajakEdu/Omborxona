from django.contrib.auth.models import User
from django.db import models

class Ombor(models.Model):
    nom = models.CharField(max_length=30)
    ism = models.CharField(max_length=30)
    manzil = models.CharField(max_length=30)
    tel = models.CharField(max_length=30)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.nom}, {self.ism}'
