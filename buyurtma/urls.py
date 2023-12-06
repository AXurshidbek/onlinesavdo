from django.urls import path
from .views import *

urlpatterns = [
    path('tanlanganlar/', TanlanganlarView.as_view()),
    path('buyurtmalar/', BuyurtmalarView.as_view()),
    path('savatlar/', SavatlarView.as_view()),
    path('t_ochir/<int:son>/', TanlanganOchir.as_view()),
    path('miqdor_q/<int:son>/', MiqdorQosh.as_view()),
    path('miqdor_k/<int:son>/', MiqdorKam.as_view()),
    path('tanlangan_qosh/<int:son>/', TanlanganQosh.as_view()),
    path('savat_ochir/<int:son>/', SavatOchir.as_view()),
]