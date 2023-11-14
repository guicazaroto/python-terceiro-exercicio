from django.contrib import admin
from .models import Disciplina
from django.contrib.admin import ModelAdmin


class DisciplinaAdmin(ModelAdmin):
  list_display = ['titulo', 'descricao', 'professor', 'setor']


admin.site.register(Disciplina, DisciplinaAdmin)
