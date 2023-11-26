from django.urls import path
from .views import *

urlpatterns = [
    path('home/', HomeView.as_view()),
    path('bolimlar/', BolimlarView.as_view()),
    path('mahsulotlar/', MahsulotlarView.as_view()),
    path('mahsulot/', MahsulotView.as_view()),
]