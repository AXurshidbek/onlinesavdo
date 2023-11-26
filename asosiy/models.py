from django.db import models

class Bolim(models.Model):
    nom=models.CharField(max_length=31)
    rasm=models.FileField(upload_to="bolimlar")

    def __str__(self):
        return self.nom
