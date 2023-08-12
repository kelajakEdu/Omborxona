from django.shortcuts import render, redirect
from .models import *
from django.views import *
from userapp.models import Ombor
from asosiy.models import *

class StatistikaView(View):
    def get(self, request):
        qidiruv = request.GET.get('soz')
        natija = Statistika.objects.filter(ombor__user=request.user)
        if qidiruv:
            natija = natija.filter(mahsulot__nom__contains=qidiruv)|natija.filter(mijoz__nom__contains=qidiruv)|natija.filter(mijoz__Ism__contains=qidiruv)
        content = {
            'stats': natija,
            'mahsulotlar': Maxsulot.objects.filter(ombor__user=request.user),
            'mijozlar': Mijoz.objects.filter(ombor__user=request.user)
        }
        return render(request, 'stats.html', content)
    def post(self, request):
        Statistika.objects.create(
            mahsulot = Maxsulot.objects.get(id=request.POST.get('pr')),
            mijoz = Mijoz.objects.get(id=request.POST.get('cl')),
            ombor = Ombor.objects.get(user=request.user),
            sana = request.POST.get('sana'),
            miqdor = request.POST.get('miqdor'),
            summa = request.POST.get('summa'),
            nasiya = request.POST.get('nasiya'),
            tolangan_summa = request.POST.get('tolandi')
        )
        mijoz = Mijoz.objects.get(id=request.POST.get('cl'))
        mijoz.qarz += int(request.POST.get('nasiya'))
        mijoz.save()
        mahsulot = Maxsulot.objects.get(id=request.POST.get('pr'))
        mahsulot.soni -= int(request.POST.get('miqdor'))
        mahsulot.save()

        return redirect('stats')
