from django.urls import path
from .views import index, pagina_principal, pagina_registro, pagina_login, pagina_front

urlpatterns = [
    path('', index, name='index'),
    path('login/', pagina_login, name='login'),
    path('registro/', pagina_registro, name='registro'),
    path('front/', pagina_front, name='pagina_front'),
    path('login/principal/', pagina_principal, name='pagina_principal'),
]
