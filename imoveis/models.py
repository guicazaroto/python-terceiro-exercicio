from django.db import models

class Imovel(models.Model):
    endereco = models.CharField(max_length=100)
    rua = models.CharField(max_length=20)
    cep = models.CharField(max_length=20)
    contato = models.CharField(max_length=15)
    aluguel = models.CharField(max_length=20)
    condominio = models.CharField(max_length=20)

    def __str__(self):
        return self.endereco
