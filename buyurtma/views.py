from django.shortcuts import render,redirect
from .models import *
from django.views import View

from asosiy.models import Mahsulot


class TanlanganlarView(View):
    def get(self,request):
        content={
            "tanlanganlar": Tanlanganlar.objects.filter(profil=request.user)
        }
        return render(request,'page-profile-wishlist.html', content)


class TanlanganOchir(View):
    def get(self,request,son):
        Tanlanganlar.objects.get(id=son).delete()
        return redirect('/buyurtma/tanlanganlar/')


class BuyurtmalarView(View):
    def get(self,request):
        return render(request,'page-profile-orders.html')


class SavatlarView(View):
    def get(self,request):
        savati=Savat.objects.filter(profil=request.user)
        if savati.exists():
            savati=savati.first()
        else:
            savati=savati.objects.create(profil=request.user)
        itemlar=SavatItem.objects.filter(savat=savati)
        chegirma=0
        for item in itemlar:
            chegirma+=(item.mahsulot.narx*item.mahsulot.chegirma)//100
        conent={
            "savat":savati,
            "itemlar":itemlar,
            "chg": chegirma,
            "sum": savati.total_sum+chegirma,
            "yakuniy":savati.total_sum,


        }
        return render(request, 'page-shopping-cart.html', conent)


class MiqdorQosh(View):
    def get(self,request,son):
        item=SavatItem.objects.get(id=son)
        item.miqdor+=1
        item.save()
        return redirect('/buyurtma/savatlar/')


class MiqdorKam(View):
    def get(self,request,son):
        item=SavatItem.objects.get(id=son)
        if item.miqdor!=1:
            item.miqdor-=1
        item.save()
        return redirect('/buyurtma/savatlar/')


class TanlanganQosh(View):
    def post(self,request,son):
        savat=SavatItem.objects.get(id=son)
        Tanlanganlar.objects.create(
            mahsulot=savat.mahsulot,
            profil=request.user
        )
        # return redirect('/buyurtma/tanlanganlar/')
    def get(self,request,son):
        return redirect('/buyurtma/tanlanganlar/')

class SavatOchir(View):
    def get(self,request,son):
        SavatItem.objects.get(id=son).delete()
        return redirect('/buyurtma/savatlar/')

class SavatQosh(View):
    def post(self,request,son):
        pass