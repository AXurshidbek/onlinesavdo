from django.shortcuts import render,redirect
from .models import *
from django.views import View

class TanlanganlarView(View):
    def get(self,request):
        return render(request,'page-profile-wishlist.html')

class BuyurtmalarView(View):
    def get(self,request):
        return render(request,'page-profile-orders.html')


class SavatlarView(View):
    def get(self,request):
        return render(request, 'page-shopping-cart.html')


