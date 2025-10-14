
from django.urls import path
<<<<<<< HEAD
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('registro/', views.pagina_registro, name='registro'),
    path('login/', views.pagina_login, name='login'),
    path('logout/', LogoutView.as_view(next_page='index'), name='logout'),
    path('', views.index, name='index'), 
    path('front/', views.pagina_front, name='pagina_front'),
]
=======
from .views import index, pagina_principal, pagina_registro, pagina_login, pagina_front

urlpatterns = [
    path('', index, name='index'),
    path('login/', pagina_login, name='login'),
    path('registro/', pagina_registro, name='registro'),
    path('front/', pagina_front, name='pagina_front'),
    path('login/principal/', pagina_principal, name='pagina_principal'),
]
>>>>>>> 8d7a46320db8db6fe3c693d59c7a040b1dbc7f68
