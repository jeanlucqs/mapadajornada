from django.contrib import admin
from django.urls import path, include
from mapa.views import (
    index,
    pagina_login,
    pagina_registro,
    pagina_principal,
    pagina_front
)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mapa.urls')),
    path('', index, name='index'),
    path('login/', pagina_login, name='login'),
    path('registro/', pagina_registro, name='registro'),
    path('front/', pagina_front, name='pagina_front'),
    path('login/principal/', pagina_principal, name='pagina_principal'),
]
