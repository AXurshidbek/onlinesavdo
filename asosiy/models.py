from django.db import models
from userapp.models import Profil

class Bolim(models.Model):
    nom=models.CharField(max_length=31)
    rasm=models.FileField(upload_to="bolimlar")

    def __str__(self):
        return self.nom

class Mahsulot(models.Model):
    nom=models.CharField(max_length=55)
    batafsil=models.TextField()
    narx=models.PositiveIntegerField()
    brend=models.CharField(max_length=25)
    chegirma=models.PositiveIntegerField(default=0)
    kafolat=models.CharField(max_length=25)
    yetkazish=models.CharField(max_length=55)
    mavjud=models.BooleanField(default=True)
    davlat=models.CharField(max_length=35)
    bolim=models.ForeignKey(Bolim, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom

class Media(models.Model):
    rasm=models.FileField()
    mahsulot=models.ForeignKey(Mahsulot, on_delete=models.CASCADE)



class Izoh(models.Model):
    profil=models.ForeignKey(Profil, on_delete=models.CASCADE)
    mahsulot=models.ForeignKey(Mahsulot, on_delete=models.CASCADE)
    matn=models.TextField()
    baho=models.PositiveSmallIntegerField(default=5)
    sana=models.DateField()

    def __str__(self):
        return self.matn


