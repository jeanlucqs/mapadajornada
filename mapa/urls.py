from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('registro/', views.pagina_registro, name='registro'),
    path('login/', views.pagina_login, name='login'),
    path('logout/', LogoutView.as_view(next_page='index'), name='logout'),
    path('', views.index, name='index'), 
    path('front/', views.pagina_front, name='pagina_front'),
    path('back/', views.pagina_back, name='pagina_back'),
    path('mobile/', views.pagina_mobile, name='pagina_mobile'),
    path('ciencia/', views.pagina_ciencia, name='pagina_ciencia'),
    path('engenharia/', views.pagina_engenharia, name='pagina_engenharia'),
    path('analista-bi/', views.pagina_analista_bi, name='pagina_analista'),
    path('analise-seguranca/', views.pagina_AnaliseSeguranca, name='pagina_analise_seguranca'),
    path('forense/', views.pagina_Forense, name='pagina_forense'),
    path('engenharia-seguranca/', views.pagina_EngenhariaSeguranca, name='pagina_engenharia_seguranca'),
    path('adm-redes/', views.pagina_AdmRedes, name='pagina_adm_redes'),
    path('arquiteto-nuvem/', views.pagina_ArquitetoNuvem, name='pagina_arquiteto_nuvem'),
    path('devops/', views.pagina_DevOps, name='pagina_devops'),
    path('ux/', views.pagina_Ux, name='pagina_ux'),
    path('ui/', views.pagina_Ui, name='pagina_ui'),
    path('pesquisador/', views.pagina_pesquisador, name='pagina_pesquisador'),
    path('trilhas/', views.trilhas, name='trilhas'),
    path('trilhas/frontend/', views.trilha_frontend, name='trilha_frontend'),
    path('trilhas/backend/', views.trilha_backend, name='trilha_backend'),
    path('trilhas/fullstack/', views.trilha_fullstack, name='trilha_fullstack'),

    path('perfil/', views.perfil, name='perfil'),
    path('perfil/editar/', views.editar_perfil, name='editar_perfil'),
    path('habilidade/adicionar/', views.adicionar_habilidade, name='adicionar_habilidade'),
    path('habilidade/editar/<int:id>/', views.editar_habilidade, name='editar_habilidade'),
    path('habilidade/excluir/<int:id>/', views.excluir_habilidade, name='excluir_habilidade'),
    path('competencia/adicionar/', views.adicionar_competencia, name='adicionar_competencia'),
    path('competencia/editar/<int:id>/', views.editar_competencia, name='editar_competencia'),
    path('competencia/excluir/<int:id>/', views.excluir_competencia, name='excluir_competencia'),
    path('projeto/adicionar/', views.adicionar_projeto, name='adicionar_projeto'),
    path('projeto/editar/<int:id>/', views.editar_projeto, name='editar_projeto'),
    path('projeto/excluir/<int:id>/', views.excluir_projeto, name='excluir_projeto'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)