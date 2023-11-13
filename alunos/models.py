from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    matricula = models.CharField(max_length=20)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    endereco = models.CharField(max_length=100, default='')
    cpf = models.CharField(max_length=11, default='')

    def __str__(self):
        return self.nome
