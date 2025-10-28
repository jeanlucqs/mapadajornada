from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomAuthenticationForm, PerfilForm, HabilidadeForm, CompetenciaForm
from .models import PaginaFrontend, PaginaBackend, PaginaMobile, Perfil, Habilidade, Competencia
from django.contrib import messages

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
    conteudo = PaginaBackend.objects.first()  
    return render(request, 'pagina_back.html', {'conteudo': conteudo})

@login_required
def pagina_mobile(request):
    conteudo = PaginaMobile.objects.first()  
    return render(request, 'pagina_mobile.html', {'conteudo': conteudo})

@login_required
def perfil(request):
    perfil = Perfil.objects.get_or_create(user=request.user)
    habilidades = Habilidade.objects.filter(user=request.user)
    competencias = Competencia.objects.filter(user=request.user)
    context ={
        'perfil': perfil,
        'habilidades': habilidades,
        'competencias': competencias,
    }
    return render(request, 'perfil.html', context)


@login_required
def editar_perfil(request):
    perfil, _ = Perfil.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = PerfilForm(request.POST, request.FILES, instance=perfil)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            messages.success(request, 'Perfil atualizado com sucesso!')
            return redirect('perfil')
    else:
        form = PerfilForm(instance=perfil)
    return render(request, 'editar_perfil.html', {'form': form})

# --- CRUD HABILIDADE ---
@login_required
def adicionar_habilidade(request):
    if request.method == 'POST':
        form = HabilidadeForm(request.POST)
        if form.is_valid():
            hab = form.save(commit=False)
            hab.user = request.user
            hab.save()
            return redirect('perfil')
    else:
        form = HabilidadeForm()
    return render(request, 'form.html', {'form': form, 'titulo': 'Adicionar Habilidade'})

@login_required
def editar_habilidade(request, id):
    hab = get_object_or_404(Habilidade, id=id, user=request.user)
    if request.method == 'POST':
        form = HabilidadeForm(request.POST, instance=hab)
        if form.is_valid():
            form.save()
            return redirect('perfil')
    else:
        form = HabilidadeForm(instance=hab)
    return render(request, 'form.html', {'form': form, 'titulo': 'Editar Habilidade'})

@login_required
def excluir_habilidade(request, id):
    hab = get_object_or_404(Habilidade, id=id, user=request.user)
    if request.method == 'POST':
        hab.delete()
        return redirect('perfil')
    return render(request, 'confirm_delete.html', {'obj': hab, 'tipo': 'habilidade'})


@login_required
def adicionar_competencia(request):
    if request.method == 'POST':
        form = CompetenciaForm(request.POST)
        if form.is_valid():
            c = form.save(commit=False)
            c.user = request.user
            c.save()
            return redirect('perfil')
    else:
        form = CompetenciaForm()
    return render(request, 'form.html', {'form': form, 'titulo': 'Adicionar Competência'})

@login_required
def editar_competencia(request, id):
    comp = get_object_or_404(Competencia, id=id, user=request.user)
    if request.method == 'POST':
        form = CompetenciaForm(request.POST, instance=comp)
        if form.is_valid():
            form.save()
            return redirect('perfil')
    else:
        form = CompetenciaForm(instance=comp)
    return render(request, 'mapa/form.html', {'form': form, 'titulo': 'Editar Competência'})

@login_required
def excluir_competencia(request, id):
    comp = get_object_or_404(Competencia, id=id, user=request.user)
    if request.method == 'POST':
        comp.delete()
        return redirect('perfil')
    return render(request, 'mapa/confirm_delete.html', {'obj': comp, 'tipo': 'competência'})