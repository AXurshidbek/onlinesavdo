from django.shortcuts import render,redirect
from django.views import View
from .models import *
from django.db.models import Avg
from userapp.models import Profil
from django.utils import timezone


class HomeLoginsizView(View):
    def get(self,request):
        content={
            "bolimlar": Bolim.objects.all()[:5],
        }
        return render(request, 'page-index-2.html', content)

class HomeView(View):
    def get(self,request):
        if request.user.is_authenticated:
            content={
                "bolimlar": Bolim.objects.all()[:8]
            }
            return render(request, 'page-index.html', content)
        return render(request, '/user/login/')


class BolimlarView(View):
    def get(self, request):
        if request.user.is_authenticated:
            content={
                "bolimlar": Bolim.objects.all(),
                "mahsulotlar": Mahsulot.objects.all(),
            }
            return render(request, 'page-category.html', content)
        return render(request, '/user/login/')


class MahsulotlarView(View):
    def get(self, request, pk):
        if request.user.is_authenticated:
            content={
                "mahsulotlar" : Mahsulot.objects.filter(bolim=pk)
            }
            return render(request, 'page-listing-grid.html', content)
        return render(request, '/user/login/')


class MahsulotView(View):

    def post(self,request,pj):
        Izoh.objects.create(
            profil=request.user,
            mahsulot=Mahsulot.objects.get(id=pj),
            matn=request.POST.get("izoh"),
            baho=request.POST.get("rating"),
            sana=timezone.now(),
        )
        return redirect('/asosiy/bolimlar/')
    def get(self,request, pj):
        izohlar=Izoh.objects.filter(mahsulot__id=pj)
        ortachasi=izohlar.aggregate(Avg("baho")).get("rating__avg")
        print(ortachasi)
        if ortachasi:
            ortachasi*=20
        else:
            ortachasi=0
        if request.user.is_authenticated:
            content={
                "mahsulot": Mahsulot.objects.get(id=pj),
                "ortachasi": ortachasi,
            }
            return render(request,'page-detail-product.html', content)
        return render(request, '/user/login/')

