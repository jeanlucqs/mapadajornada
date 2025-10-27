from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from .models import PaginaFrontend, PaginaBackend

def index(request):
    return render(request, 'index.html')

def pagina_principal(request):
    return render(request, 'principal.html')

def pagina_registro(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'registro.html', {'form': form})


def pagina_login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'login.html', {'form': form})


@login_required
def pagina_front(request):
    conteudo = PaginaFrontend.objects.first()
    return render(request, 'pagina_front.html', {'conteudo': conteudo})

@login_required
def pagina_back(request):
    conteudo = PaginaBackend.objects.first()  # pega o primeiro registro
    return render(request, 'pagina_back.html', {'conteudo': conteudo})
