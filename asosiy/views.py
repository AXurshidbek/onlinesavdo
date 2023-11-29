from django.shortcuts import render
from django.views import View
from .models import *
from django.db.models import Avg

class HomeLoginsizView(View):
    def get(self,request):
        return render(request, 'page-index-2.html')

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
    def get(self,request, pj):
        izohlar=Izoh.objects.filter(mahsulot__id=pj)
        ortachasi=izohlar.aggregate(Avg("baho")).get("rating__avg")
        if ortachasi:
            ortachasi*=20
        else:
            ortachasi=0
        if request.user.is_authenticated:
            content={
                "mahsulot": Mahsulot.objects.get(id=pj)
            }
            return render(request,'page-detail-product.html', content)
        return render(request, '/user/login/')
