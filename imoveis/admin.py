from django.contrib import admin
from .models import Imovel
from django.contrib.admin import ModelAdmin


class ImovelAdmin(ModelAdmin):
  list_display = ['endereco', 'rua', 'aluguel', 'condominio']


admin.site.register(Imovel, ImovelAdmin)
