from django.shortcuts import render, redirect
from .models import *
from django.views import *
from userapp.models import Ombor
from asosiy.models import Mijoz


def home(request):
    return render(request, 'home.html')

# def bulimlar(request):
#     return render(request, 'bulimlar.html')

def client_update(request):
    return render(request, 'client_update.html')

def clients(request):
    return render(request, 'clients.html')

def product_update(request):
    return render(request, 'product_update.html')

def products(request):
    return render(request, 'products.html')

def stats(request):
    return render(request, 'stats.html')



def mahsulotlar(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            pr_nom=request.POST.get('pr_name')
            pr_brand=request.POST.get('pr_brand')
            pr_narx=request.POST.get('pr_narx')
            pr_soni=request.POST.get('pr_soni')
            pr_sana=request.POST.get('pr_date')
            pr_olchov=request.POST.get('pr_miqdor')
            pr_ombor=Ombor.objects.get(user=request.user)
            Maxsulot.objects.create(nom=pr_nom, brand=pr_brand, narx=pr_narx, soni=pr_soni, olchov=pr_olchov, ombor=pr_ombor, sana=pr_sana)
            return redirect('/products/')

    if request.method == 'GET':
        natija = Maxsulot.objects.filter(ombor=Ombor.objects.get(user=request.user))
        qidiruv_sozi = request.GET.get('search')
        if qidiruv_sozi:
            natija = natija.filter(nom__contains=qidiruv_sozi)|natija.filter(brand__contains=qidiruv_sozi)
        content = {
            'mahsulotlar': natija
        }
    return render(request, 'products.html', content)

# def mijozlar(request):
#     if request.user.is_authenticated:
#         content = {
#             'mijoz': Mijoz.objects.filter(ombor__user=request.user)
#         }
#         return render(request, 'clients.html', content)


def product_delete(request, son):
    if request.user.is_authenticated:
        content = {
            'delete': Maxsulot.objects.filter(id=son).delete()
        }
        return redirect('/products/')


def client_del(request, son):
    if request.user.is_authenticated:
        content = {
            'del': Mijoz.objects.filter(id=son).delete()
        }
        return redirect('/clients/')

def ombor_for(request):
    if request.user.is_authenticated:
        content = {
            'ombor_name': Ombor.objects.all()
        }
        return render(request, 'products.html', content)

class MahsulotUpdate(View):
    def get(self, request, pk):
        content={
            'product': Maxsulot.objects.get(id=pk),
            'olchov': ['dona', 'block', 'l', 'kg']
        }
        return render(request, 'product_update.html', content)
    def post(self, request, pk):
        Maxsulot.objects.filter(id=pk).update(
            soni = request.POST.get('s'),
            narx = request.POST.get('price'),
            olchov = request.POST.get('m'),
        )
        return redirect('/products/')

# def mijozlar(request):
#     if request.user.is_authenticated:
#         all_client = Mijoz.objects.filter(ombor__user=request.user)
#         if request.method == 'POST':
#             soz = request.POST.get('seorch_client')
#             all_client = Mijoz.objects.filter(ombor__user=request.user, Ism__contains=soz)|Mijoz.objects.filter(ombor__user=request.user, nom__contains=soz)
#         content = {
#             'mijoz': all_client
#         }
#         return render(request, 'clients.html', content)

class Mijoz_view(View):
    def get(self, request):
        all_client = Mijoz.objects.filter(ombor__user = request.user)
        qid_soz = request.GET.get('seorch_client')
        if qid_soz:
            all_client=Mijoz.objects.filter(ombor__user = request.user, Ism__contains=qid_soz)
        content={
            'mijozlar': all_client
        }
        return render(request, 'clients.html', content)
