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
    perfil, _ = Perfil.objects.get_or_create(user=request.user)
    habilidades = Habilidade.objects.filter(user=request.user)
    competencias = Competencia.objects.filter(user=request.user)

    context = {
        'perfil': perfil,
        'habilidades': habilidades,
        'competencias': competencias,
    }
    return render(request, 'perfil.html', context)


# ---------------- EDITAR PERFIL ----------------
@login_required
def editar_perfil(request):
    perfil, _ = Perfil.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = PerfilForm(request.POST, request.FILES, instance=perfil)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            messages.success(request, 'Perfil atualizado com sucesso!')
            # ✅ Redireciona para a página de perfil
            return redirect('perfil')
    else:
        form = PerfilForm(instance=perfil)

    habilidades = Habilidade.objects.filter(user=request.user)
    competencias = Competencia.objects.filter(user=request.user)

    context = {
        'form': form,
        'perfil': perfil,
        'habilidades': habilidades,
        'competencias': competencias,
    }
    return render(request, 'editar_perfil.html', context)


# ---------------- HABILIDADES ----------------
@login_required
def adicionar_habilidade(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        if nome:
            Habilidade.objects.create(user=request.user, nome=nome)
            messages.success(request, f'Habilidade "{nome}" adicionada com sucesso!')
        else:
            messages.error(request, 'Digite o nome da habilidade antes de adicionar.')
        return redirect('editar_perfil')
    return redirect('editar_perfil')


@login_required
def editar_habilidade(request, id):
    hab = get_object_or_404(Habilidade, id=id, user=request.user)
    if request.method == 'POST':
        form = HabilidadeForm(request.POST, instance=hab)
        if form.is_valid():
            form.save()
            messages.success(request, 'Habilidade atualizada com sucesso!')
            return redirect('editar_perfil')
    else:
        form = HabilidadeForm(instance=hab)
    return render(request, 'form.html', {'form': form, 'titulo': 'Editar Habilidade'})


@login_required
def excluir_habilidade(request, id):
    hab = get_object_or_404(Habilidade, id=id, user=request.user)
    if request.method == 'POST':
        nome = hab.nome
        hab.delete()
        messages.success(request, f'Habilidade "{nome}" excluída com sucesso!')
        return redirect('editar_perfil')
    return render(request, 'confirm_delete.html', {'obj': hab, 'tipo': 'habilidade'})


# ---------------- COMPETÊNCIAS ----------------
@login_required
def adicionar_competencia(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        if nome:
            Competencia.objects.create(user=request.user, nome=nome)
            messages.success(request, f'Competência "{nome}" adicionada com sucesso!')
        else:
            messages.error(request, 'Digite o nome da competência antes de adicionar.')
        return redirect('editar_perfil')
    return redirect('editar_perfil')


@login_required
def editar_competencia(request, id):
    comp = get_object_or_404(Competencia, id=id, user=request.user)
    if request.method == 'POST':
        form = CompetenciaForm(request.POST, instance=comp)
        if form.is_valid():
            form.save()
            messages.success(request, 'Competência atualizada com sucesso!')
            return redirect('editar_perfil')
    else:
        form = CompetenciaForm(instance=comp)
    return render(request, 'form.html', {'form': form, 'titulo': 'Editar Competência'})


@login_required
def excluir_competencia(request, id):
    comp = get_object_or_404(Competencia, id=id, user=request.user)
    if request.method == 'POST':
        nome = comp.nome
        comp.delete()
        messages.success(request, f'Competência "{nome}" excluída com sucesso!')
        return redirect('editar_perfil')
    return render(request, 'confirm_delete.html', {'obj': comp, 'tipo': 'competência'})