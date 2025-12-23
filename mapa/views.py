from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import CustomUserCreationForm, CustomAuthenticationForm, PerfilForm, HabilidadeForm, CompetenciaForm, ProjetoForm, TrilhaForm, CarreiraForm

# --- IMPORTAÇÃO CORRIGIDA (Sem TrilhaModulo e TrilhaTopico) ---
from .models import (
    PaginaFrontend, PaginaBackend, PaginaMobile, PaginaCiencia, PaginaEngenharia, 
    Perfil, Habilidade, Competencia, Categoria, Projeto, 
    PaginaAnalistaBI, PaginaAnaliseSeguranca, PaginaForense, PaginaEngenhariaSeguranca, 
    PaginaAdmRedes, PaginaArquitetoNuvem, PaginaDevOps, PaginaUx, PaginaUi, PaginaPesquisador,
    Trilha, Carreira 
)

# --- VIEWS PÚBLICAS ---

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
            next_url = request.POST.get('next') or request.GET.get('next')
            if next_url:
                return redirect(next_url)
            else:
                return redirect('index')      
    else:
        form = CustomAuthenticationForm()
    return render(request, 'login.html', {'form': form})

# --- VIEWS DE TRILHAS (SISTEMA HÍBRIDO) ---

@login_required
def trilhas(request):
    # Lista os cards das trilhas cadastrados no banco
    trilhas_list = Trilha.objects.all().order_by('ordem')
    return render(request, 'trilhas.html', {'trilhas_list': trilhas_list})

# Views Estáticas (Onde os cards clicados vão dar)
@login_required
def trilha_frontend(request):
    return render(request, 'trilha_frontend.html')

@login_required
def trilha_backend(request):
    return render(request, 'trilha_backend.html') 

@login_required
def trilha_devops(request):
    return render(request, 'trilha_devops.html')

@login_required
def trilha_analseguranca(request):
    return render(request, 'trilha_analseguranca.html')

@login_required
def trilha_mobile(request):
    return render(request, 'trilha_mobile.html')

@login_required
def trilha_ciencia_dados(request):
    return render(request, 'trilha_ciencia_dados.html')

@login_required
def trilha_engenheiro_dados(request):
    return render(request, 'trilha_engenheiro_dados.html')

@login_required
def trilha_forensedig(request):
    return render(request, 'trilha_forensedig.html')

@login_required
def trilha_engdevops(request):
    return render(request, 'trilha_engdevops.html')

@login_required
def trilha_designerui(request):
    return render(request, 'trilha_designerui.html')

@login_required
def trilha_designerux(request):
    return render(request, 'trilha_designerux.html')

@login_required
def trilha_pesquisadorux(request):
    return render(request, 'trilha_pesquisadorux.html')

@login_required
def trilha_engsegur(request):
    return render(request, 'trilha_engsegur.html')

@login_required
def trilha_arqnuvem(request):
    return render(request, 'trilha_arqnuvem.html')

@login_required
def trilha_admredes(request):
    return render(request, 'trilha_admredes.html')

@login_required
def trilha_bi(request):
    return render(request, 'trilha_bi.html')

@login_required
def trilha_engenharia_seguranca(request):
    return render(request, 'trilha_engenharia_seguranca.html')

@login_required
def analise_seguranca(request):
    return render(request, 'trilha_analise_seguranca.html')

@login_required
def forense(request):
    return render(request, 'trilha_forense.html')

@login_required
def adm_redes(request): 
    return render(request, 'trilha_adm_redes.html')


# --- VIEWS ANTIGAS (LEGADO - MANTIDAS PARA NÃO QUEBRAR) ---

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
def pagina_AdmRedes(request):
    area = PaginaAdmRedes.objects.first()
    return render(request, 'pagina_adm_redes.html', {'area': area})

@login_required
def pagina_ArquitetoNuvem(request):
    area = PaginaArquitetoNuvem.objects.first()
    return render(request, 'pagina_arquiteto_nuvem.html', {'area': area})

@login_required
def pagina_DevOps(request):
    area = PaginaDevOps.objects.first()
    return render(request, 'pagina_devops.html', {'area': area})

@login_required
def pagina_Ux(request):
    area = PaginaUx.objects.first()
    return render(request, 'pagina_ux.html', {'area': area})

@login_required
def pagina_Ui(request):
    area = PaginaUi.objects.first()
    return render(request, 'pagina_ui.html', {'area': area})

@login_required
def pagina_pesquisador(request):
    area = PaginaPesquisador.objects.first()
    return render(request, 'pagina_pesquisador.html', {'area': area})


# --- PERFIL E CRUD DE USUÁRIO ---

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

@login_required
def editar_perfil(request):
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
                    Habilidade.objects.get_or_create(user=request.user, nome=nome_habilidade.strip())
            
            # Processar novas competências
            novas_competencias = request.POST.getlist('competencias')
            for nome_competencia in novas_competencias:
                if nome_competencia.strip():
                    Competencia.objects.get_or_create(user=request.user, nome=nome_competencia.strip())
            
            messages.success(request, 'Perfil atualizado com sucesso!')
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
    return render(request, 'projeto_form.html', {'form': form, 'titulo': 'Editar Projeto'})

@login_required
def excluir_projeto(request, id):
    projeto = get_object_or_404(Projeto, id=id, user=request.user)
    if request.method == 'POST':
        nome = projeto.titulo
        projeto.delete()
        messages.success(request, f'Projeto "{nome}" excluído com sucesso!')
        return redirect('perfil')
    return render(request, 'confirm_delete.html', {'obj': projeto, 'tipo': 'projeto'})


# --- DASHBOARD & CRUD ADMINISTRATIVO ---

def check_admin(user):
    return user.is_superuser

@login_required
@user_passes_test(check_admin)
def dashboard(request):
    # Estatísticas
    total_users = User.objects.count()
    total_trilhas = Trilha.objects.count()
    total_carreiras = Carreira.objects.count()
    total_projetos = Projeto.objects.count()
    
    # Listas
    trilhas = Trilha.objects.all().order_by('titulo')
    carreiras = Carreira.objects.all().order_by('titulo')
    ultimos_usuarios = User.objects.all().order_by('-date_joined')[:5]

    context = {
        'total_users': total_users,
        'total_trilhas': total_trilhas,
        'total_carreiras': total_carreiras,
        'total_projetos': total_projetos,
        'trilhas': trilhas,
        'carreiras': carreiras,
        'ultimos_usuarios': ultimos_usuarios
    }
    return render(request, 'dashboard.html', context)

# CRUD DELETE TRILHA
@login_required
@user_passes_test(check_admin)
def deletar_trilha(request, id):
    trilha = get_object_or_404(Trilha, id=id)
    nome = trilha.titulo
    trilha.delete()
    messages.success(request, f'Trilha "{nome}" removida com sucesso!')
    return redirect('dashboard')

# CRUD DELETE CARREIRA
@login_required
@user_passes_test(check_admin)
def deletar_carreira(request, id):
    carreira = get_object_or_404(Carreira, id=id)
    nome = carreira.titulo
    carreira.delete()
    messages.success(request, f'Carreira "{nome}" removida com sucesso!')
    return redirect('dashboard')

@login_required
@user_passes_test(check_admin)
def gerenciar_trilha(request, id=None):
    # Se tem ID, é edição. Se não tem, é criação.
    if id:
        trilha = get_object_or_404(Trilha, id=id)
        titulo_pag = f"Editar Trilha: {trilha.titulo}"
    else:
        trilha = None
        titulo_pag = "Nova Trilha"

    if request.method == 'POST':
        form = TrilhaForm(request.POST, instance=trilha)
        if form.is_valid():
            form.save()
            messages.success(request, 'Trilha salva com sucesso!')
            return redirect('dashboard')
    else:
        form = TrilhaForm(instance=trilha)

    return render(request, 'form_dashboard.html', {'form': form, 'titulo': titulo_pag})

# 2. CARREIRAS
@login_required
@user_passes_test(check_admin)
def gerenciar_carreira(request, id=None):
    # Se tem ID, é edição. Se não tem, é criação.
    if id:
        carreira = get_object_or_404(Carreira, id=id)
        titulo_pag = f"Editar Carreira: {carreira.titulo}"
    else:
        carreira = None
        titulo_pag = "Nova Carreira"

    if request.method == 'POST':
        form = CarreiraForm(request.POST, instance=carreira)
        if form.is_valid():
            form.save()
            messages.success(request, 'Carreira salva com sucesso!')
            return redirect('dashboard')
    else:
        form = CarreiraForm(instance=carreira)

    return render(request, 'form_dashboard.html', {'form': form, 'titulo': titulo_pag})