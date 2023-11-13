from django.contrib import admin
from .models import Carro

from django.contrib.admin import ModelAdmin


class CarroAdmin(ModelAdmin):
  list_display = ['modelo', 'fabricante', 'preco', 'cambio']

admin.site.register(Carro, CarroAdmin)
