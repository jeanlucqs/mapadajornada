from django.contrib import admin
from .models import PaginaFrontend, PaginaBackend, PaginaMobile


@admin.register(PaginaFrontend)
class PaginaFrontendAdmin(admin.ModelAdmin):
    list_display = ('titulo_principal', 'atualizado_em')


@admin.register(PaginaBackend)
class PaginaBackAdmin(admin.ModelAdmin):
    list_display = ['titulo_principal', 'faixa_junior', 'faixa_pleno', 'faixa_senior']


@admin.register(PaginaMobile)
class PaginaMobileAdmin(admin.ModelAdmin):
    list_display = ['titulo_principal', 'faixa_junior', 'faixa_pleno', 'faixa_senior']