from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomAuthenticationForm, PerfilForm, HabilidadeForm, CompetenciaForm, ProjetoForm
from .models import PaginaFrontend, PaginaBackend, PaginaMobile,PaginaCiencia,PaginaEngenharia, Perfil, Habilidade, Competencia, Categoria, Carreira, Projeto, PaginaAnalistaBI, PaginaAnaliseSeguranca, PaginaForense, PaginaEngenhariaSeguranca
from django.contrib import messages

def index(request):
    categorias = Categoria.objects.prefetch_related('carreiras').order_by('ordem')
    context = {
        'categorias_list': categorias
    }
    return render(request, 'index.html', context)

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
    area = PaginaFrontend.objects.first()
    return render(request, 'pagina_front.html', {'area': area})

@login_required
def pagina_back(request):
    area = PaginaBackend.objects.last()
    return render(request, 'pagina_back.html', {'area': area})

@login_required
def pagina_mobile(request):
    area = PaginaMobile.objects.last()
    return render(request, 'pagina_mobile.html', {'area': area})

@login_required
def pagina_ciencia(request):
    area = PaginaCiencia.objects.first()
    return render(request, 'pagina_ciencia.html', {'area': area})


@login_required
def pagina_engenharia(request):
    area = PaginaEngenharia.objects.first()
    return render(request, 'pagina_engenharia.html', {'area': area})

@login_required
def pagina_analista_bi(request):
    area = PaginaAnalistaBI.objects.first()
    return render(request, 'pagina_analista.html', {'area': area})

@login_required
def pagina_AnaliseSeguranca(request):
    area = PaginaAnaliseSeguranca.objects.first()
    return render(request, 'pagina_analise_seguranca.html', {'area': area})

@login_required
def pagina_Forense(request):
    area = PaginaForense.objects.first()
    return render(request, 'pagina_forense.html', {'area': area})

@login_required
def pagina_EngenhariaSeguranca(request):
    area = PaginaEngenhariaSeguranca.objects.first()
    return render(request, 'pagina_engenharia_seguranca.html', {'area': area})


@login_required
def perfil(request):
    perfil, created = Perfil.objects.get_or_create(user=request.user)
    habilidades = Habilidade.objects.filter(user=request.user)
    competencias = Competencia.objects.filter(user=request.user)
    projetos = Projeto.objects.filter(user=request.user)

    context = {
        'perfil': perfil,
        'habilidades': habilidades,
        'competencias': competencias,
        'projetos': projetos,
    }
    return render(request, 'perfil.html', context)


# ---------------- EDITAR PERFIL ----------------
@login_required
def editar_perfil(request):
    # CORREÇÃO: Desempacotar a tupla
    perfil, created = Perfil.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = PerfilForm(request.POST, request.FILES, instance=perfil)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            
            # Processar novas habilidades
            novas_habilidades = request.POST.getlist('habilidades')
            for nome_habilidade in novas_habilidades:
                if nome_habilidade.strip():
                    Habilidade.objects.get_or_create(
                        user=request.user, 
                        nome=nome_habilidade.strip()
                    )
            
            # Processar novas competências
            novas_competencias = request.POST.getlist('competencias')
            for nome_competencia in novas_competencias:
                if nome_competencia.strip():
                    Competencia.objects.get_or_create(
                        user=request.user, 
                        nome=nome_competencia.strip()
                    )
            
            messages.success(request, 'Perfil atualizado com sucesso!')
            return redirect('perfil')
    else:
        form = PerfilForm(instance=perfil)

    habilidades = Habilidade.objects.filter(user=request.user)
    competencias = Competencia.objects.filter(user=request.user)

    context = {
        'form': form,
        'perfil': perfil,  # Agora é o objeto, não a tupla
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

@login_required
def adicionar_projeto(request):
    if request.method == 'POST':
        form = ProjetoForm(request.POST)
        if form.is_valid():
            projeto = form.save(commit=False)
            projeto.user = request.user
            projeto.save()
            messages.success(request, f'Projeto "{projeto.titulo}" adicionado com sucesso!')
            return redirect('perfil')
    else:
        form = ProjetoForm()
    return render(request, 'projeto_form.html', {'form': form, 'titulo': 'Adicionar Novo Projeto'})


@login_required
def editar_projeto(request, id):
    projeto = get_object_or_404(Projeto, id=id, user=request.user)
    if request.method == 'POST':
        form = ProjetoForm(request.POST, instance=projeto)
        if form.is_valid():
            form.save()
            messages.success(request, f'Projeto "{projeto.titulo}" atualizado com sucesso!')
            return redirect('perfil')
    else:
        form = ProjetoForm(instance=projeto)
    return render(request, 'projeto_form.html', {'form': form, 'titulo': 'Adicionar Novo Projeto'})


@login_required
def excluir_projeto(request, id):
    projeto = get_object_or_404(Projeto, id=id, user=request.user)
    if request.method == 'POST':
        nome = projeto.titulo
        projeto.delete()
        messages.success(request, f'Projeto "{nome}" excluído com sucesso!')
        return redirect('perfil')
    return render(request, 'confirm_delete.html', {'obj': projeto, 'tipo': 'projeto'})