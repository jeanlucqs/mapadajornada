from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('registro/', views.pagina_registro, name='registro'),
    path('login/', views.login, name='login'),
    path('logout/', LogoutView.as_view(next_page='index'), name='logout'),
    path('', views.index, name='index'), 
    path('front/', views.front, name='pagina_front'),
]