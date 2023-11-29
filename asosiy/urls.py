from django.urls import path
from .views import *

urlpatterns = [
    path('home/', HomeView.as_view()),
    path('bolimlar/', BolimlarView.as_view()),
    path('bolim/<int:pk>', MahsulotlarView.as_view()),
    path('mahsulot/<int:pj>', MahsulotView.as_view()),
]