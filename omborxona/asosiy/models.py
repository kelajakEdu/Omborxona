from django.db import models
from userapp.models import Ombor

class Maxsulot(models.Model):
    nom = models.CharField(max_length=30)
    brand = models.CharField(max_length=30)
    narx = models.PositiveIntegerField()
    soni = models.PositiveIntegerField(default=0)
    olchov = models.CharField(max_length=30, choices=(('kg', 'kg'), ('l', 'l'), ('dona', 'dona'), ('block', 'block')))
    sana = models.DateField()
    ombor = models.ForeignKey(Ombor, models.CASCADE)
    def __str__(self):
        return self.nom

class Mijoz(models.Model):
    nom = models.CharField(max_length=30)
    Ism = models.CharField(max_length=30)
    tel = models.CharField(max_length=30)
    manzil = models.CharField(max_length=30)
    ombor = models.ForeignKey(Ombor, models.CASCADE)
    qarz = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.nom
