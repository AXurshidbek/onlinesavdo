from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.views import View
from .models import *

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
        return render(request,'page-user-login.html')

class RegisterView(View):
    def post(self,request):
        try:
            User.objects.create_user(
                username=request.POST.get("username"),
                email=request.POST.get("email"),
                password=request.POST.get("password")
            )
        finally:
            return redirect('/user/login')
    def get(self,request):
        return render(request,'page-user-register.html')