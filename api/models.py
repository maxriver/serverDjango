from typing import Any
from django.db import models

# Create your models here. GESTISCE I DATI CHE ARRIVANO DAL DATABASE
class Api1(models.Model):
    immagine = models.ImageField()
    descrizione = models.CharField(max_length=20)
    dato = models.FloatField()

    def __str__(self):
        return self.descrizione

