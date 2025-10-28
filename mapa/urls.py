from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('registro/', views.pagina_registro, name='registro'),
    path('login/', views.pagina_login, name='login'),
    path('logout/', LogoutView.as_view(next_page='index'), name='logout'),
    path('', views.index, name='index'), 
    path('front/', views.pagina_front, name='pagina_front'),
    path('back/', views.pagina_back, name='pagina_back'),
    path('mobile/', views.pagina_mobile, name='pagina_mobile'),
    path('perfil/', views.perfil, name='perfil'),
    path('perfil/editar/', views.editar_perfil, name='editar_perfil'),
    path('habilidade/adicionar/', views.adicionar_habilidade, name='adicionar_habilidade'),
    path('habilidade/editar/<int:id>/', views.editar_habilidade, name='editar_habilidade'),
    path('habilidade/excluir/<int:id>/', views.excluir_habilidade, name='excluir_habilidade'),
    path('competencia/adicionar/', views.adicionar_competencia, name='adicionar_competencia'),
    path('competencia/editar/<int:id>/', views.editar_competencia, name='editar_competencia'),
    path('competencia/excluir/<int:id>/', views.excluir_competencia, name='excluir_competencia'),
]