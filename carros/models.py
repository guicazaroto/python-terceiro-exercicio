from django.db import models

from django.db import models

class Carro(models.Model):
    fabricante = models.CharField(max_length=20)
    km = models.CharField(max_length=20)
    preco = models.CharField(max_length=20)
    cor = models.CharField(max_length=20)
    cambio = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20)

    def __str__(self):
        return self.modelo
