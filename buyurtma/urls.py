from django.urls import path
from .views import *

urlpatterns = [
    path('tanlanganlar/', TanlanganlarView.as_view()),
    path('buyurtmalar/', BuyurtmalarView.as_view()),
    path('savatlar/', SavatlarView.as_view()),
]