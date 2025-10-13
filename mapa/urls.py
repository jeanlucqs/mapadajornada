from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagina_registro, name='home'),
    path('registro/', views.pagina_registro, name='registro'),
    path('login/', views.pagina_login, name='login'),
    path('principal/', views.pagina_principal, name='pagina_principal'),
]