from django.contrib import admin
from .models import PaginaFrontend

@admin.register(PaginaFrontend)
class PaginaFrontendAdmin(admin.ModelAdmin):
    list_display = ('titulo_principal', 'atualizado_em')
