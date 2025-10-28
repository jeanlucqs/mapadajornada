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
]