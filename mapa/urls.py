from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('registro/', views.pagina_registro, name='registro'),
    path('login/', views.pagina_login, name='login'),
    path('front/', views.pagina_front, name='pagina_front'),
]