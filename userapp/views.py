from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.views import View
from django.conf import settings
from .models import *
from eskiz.client import SMSClient
from django.contrib.auth import login,logout,authenticate
import random

class LoginView(View):
    def post(self,request):
        user = authenticate(
            username=request.POST.get('username'),
            password=request.POST.get('password')
        )
        if user:
            login(request, user)
            return redirect('/asosiy/bolimlar/')
        return redirect('/user/login/')


    def get(self,request):
        if request.user.is_authenticated and request.user.tasdiqlangan:
            return render(request,'page-user-login.html')
        elif request.user.tasdiqlangan==False:
            return redirect('/user/tasdiqlangan/')
        return redirect('/user/login/')
class RegisterView(View):
    def post(self,request):

        profil=Profil.objects.create_user(
            username=request.POST.get("pn"),
            password=request.POST.get("ps1"),
            tel=request.POST.get("pn"),
            first_name=request.POST.get("fn"),
            last_name=request.POST.get("ln"),
            davlat=request.POST.get("country"),
            shahar=request.POST.get("city"),
            jins=request.POST.get("gender"),
            tasdiqlash_kodi=str(random.randrange(10000,100000))
        )
        mijoz=SMSClient(
            api_url = "https://notify.eskiz.uz/api/",
            email=settings.ESKIZ_GMAIL,
            password=settings.ESKIZ_PAROL,
        )
        mijoz._send_sms(
            phone_number=profil.tel,
            message=f"Online do'kondan ro'yhatdan o'tdingiz "
                    f"Sizning tasdiqlash kodingiz  {profil.tasdiqlash_kodi}"
        )
        login(request,profil)
        return redirect('/user/tasdiqlash/')
    def get(self,request):
        return render(request,'page-user-register.html')

class KodTasdiqlash(View):
    def get(self,request):

        return render(request, 'confirm.html')

    def post(self,request):
        profil=Profil.objects.get(id=request.user.id)
        if profil.tasdiqlash_kodi==request.POST.get("kod"):
            profil.tasdiqlangan=True
            profil.save()
            return redirect('/user/login/')
        return redirect('/user/tasdiqlash/')