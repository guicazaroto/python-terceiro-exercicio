from django.contrib import admin
from .models import Aluno
from django.contrib.admin import ModelAdmin


class AlunoAdmin(ModelAdmin):
  list_display = ['nome', 'cpf', 'matricula', 'telefone']


admin.site.register(Aluno, AlunoAdmin)
