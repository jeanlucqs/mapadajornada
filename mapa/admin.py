from django.contrib import admin
from .models import (
    # Páginas Estáticas (Legado)
    PaginaFrontend, PaginaBackend, PaginaMobile, PaginaCiencia, PaginaEngenharia, 
    PaginaAnalistaBI, PaginaAnaliseSeguranca, PaginaForense, PaginaEngenhariaSeguranca, 
    PaginaAdmRedes, PaginaArquitetoNuvem, PaginaDevOps, PaginaUx, PaginaUi, PaginaPesquisador,
    # Sistemas Dinâmicos
    Categoria, Carreira, Projeto,
    # SISTEMA DE TRILHA SIMPLIFICADO
    Trilha
)

# =======================================================
# 1. SISTEMA DE TRILHAS (SIMPLIFICADO)
# =======================================================

@admin.register(Trilha)
class TrilhaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'url_nome', 'ordem')
    list_editable = ('ordem',)
    search_fields = ('titulo', 'descricao')
    ordering = ('ordem',)

# =======================================================
# 2. SISTEMA DE CARREIRAS E CATEGORIAS
# =======================================================

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ordem')
    list_editable = ('ordem',)

@admin.register(Carreira)
class CarreiraAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria', 'url_nome', 'ordem')
    list_editable = ('categoria', 'ordem')
    list_filter = ('categoria',)
    search_fields = ('titulo', 'descricao')

# =======================================================
# 3. PROJETOS DOS USUÁRIOS
# =======================================================

@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'user', 'link_repositorio')
    list_filter = ('user',)
    search_fields = ('titulo', 'descricao')

# =======================================================
# 4. PÁGINAS ESTÁTICAS (LEGADO / TEXTOS FIXOS)
# =======================================================

@admin.register(PaginaFrontend)
class PaginaFrontendAdmin(admin.ModelAdmin):
    list_display = ('titulo_principal', 'atualizado_em')

@admin.register(PaginaBackend)
class PaginaBackAdmin(admin.ModelAdmin):
    list_display = ['titulo_principal', 'faixa_junior', 'faixa_pleno', 'faixa_senior']

@admin.register(PaginaMobile)
class PaginaMobileAdmin(admin.ModelAdmin):
    list_display = ['titulo_principal', 'faixa_junior', 'faixa_pleno', 'faixa_senior']

@admin.register(PaginaCiencia)
class PaginaCienciaAdmin(admin.ModelAdmin):
    list_display = ['titulo_principal', 'faixa_junior', 'faixa_pleno', 'faixa_senior']

@admin.register(PaginaEngenharia)
class PaginaEngenhariaAdmin(admin.ModelAdmin):
    list_display = ['titulo_principal', 'faixa_junior', 'faixa_pleno', 'faixa_senior']

@admin.register(PaginaAnalistaBI)
class PaginaAnalistaAdmin(admin.ModelAdmin):
    list_display = ['titulo_principal', 'faixa_junior', 'faixa_pleno', 'faixa_senior']

@admin.register(PaginaAnaliseSeguranca)
class PaginaAnaliseSegurancaAdmin(admin.ModelAdmin):
    list_display = ['titulo_principal', 'faixa_junior', 'faixa_pleno', 'faixa_senior']

@admin.register(PaginaForense)
class PaginaForenseAdmin(admin.ModelAdmin):
    list_display = ['titulo_principal', 'faixa_junior', 'faixa_pleno', 'faixa_senior']

@admin.register(PaginaEngenhariaSeguranca)
class PaginaEngenhariaSegurancaAdmin(admin.ModelAdmin):
    list_display = ['titulo_principal', 'faixa_junior', 'faixa_pleno', 'faixa_senior']

@admin.register(PaginaAdmRedes)
class PaginaAdmRedesAdmin(admin.ModelAdmin):   
    list_display = ['titulo_principal', 'faixa_junior', 'faixa_pleno', 'faixa_senior']

@admin.register(PaginaArquitetoNuvem)
class PaginaArquitetoNuvemAdmin(admin.ModelAdmin):   
    list_display = ['titulo_principal', 'faixa_junior', 'faixa_pleno', 'faixa_senior']

@admin.register(PaginaDevOps)
class PaginaDevOpsAdmin(admin.ModelAdmin):
    list_display = ['titulo_principal', 'faixa_junior', 'faixa_pleno', 'faixa_senior']

@admin.register(PaginaUx)
class PaginaUxAdmin(admin.ModelAdmin):
    list_display = ['titulo_principal', 'faixa_junior', 'faixa_pleno', 'faixa_senior']

@admin.register(PaginaUi)
class PaginaUiAdmin(admin.ModelAdmin):
    list_display = ['titulo_principal', 'faixa_junior', 'faixa_pleno', 'faixa_senior']

@admin.register(PaginaPesquisador)
class PaginaPesquisadorAdmin(admin.ModelAdmin):
    list_display = ['titulo_principal', 'faixa_junior', 'faixa_pleno', 'faixa_senior']