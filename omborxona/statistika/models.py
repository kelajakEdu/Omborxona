from django.db import models
from asosiy.models import Maxsulot, Mijoz
from userapp.models import Ombor

class Statistika(models.Model):
    mahsulot = models.ForeignKey(Maxsulot, on_delete=models.CASCADE)
    mijoz = models.ForeignKey(Mijoz, on_delete=models.CASCADE)
    ombor = models.ForeignKey(Ombor, on_delete=models.CASCADE)
    miqdor = models.PositiveSmallIntegerField()
    sana = models.DateTimeField()
    summa = models.PositiveIntegerField()
    tolangan_summa = models.PositiveIntegerField()
    nasiya = models.PositiveIntegerField()

    def save(self, *args, **kwargs):
        self.summa = int(self.miqdor) * int(self.mahsulot.narx)
        self.nasiya = int(self.summa) - int(self.tolangan_summa)
        super(Statistika, self).save(*args, **kwargs)