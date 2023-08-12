from django.conf import settings
from django.contrib import admin
from django.urls import path
from asosiy.views import *
from statistika.views import *
from userapp.views import *
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_view),
    path('logout_view/', logout_view, name='logout'),
    path('bulimlar/', bulimlar),
    path('stats/', stats),
    # path('products/', ombor_for),
    path('products/', mahsulotlar),
    path('mahsulot_delete/<int:son>', product_delete),
    path('product_update/', product_update),
    # path('clients/', mijozlar),
    path('clients/', Mijoz_view.as_view()),
    path('client_delete/<int:son>', client_del),
    path('client_update/', client_update),
    path('bulimlar/', bulimlar),
    path('product_update/<int:pk>', MahsulotUpdate.as_view()),
    path('statistikalar/', StatistikaView.as_view(), name='stats'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
