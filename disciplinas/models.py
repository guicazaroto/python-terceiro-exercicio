from django.db import models

class Disciplina(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=20)
    duracao = models.EmailField()
    professor = models.CharField(max_length=15)
    codigo = models.CharField(max_length=100, default='')
    setor = models.CharField(max_length=11, default='')

    def __str__(self):
        return self.nome
