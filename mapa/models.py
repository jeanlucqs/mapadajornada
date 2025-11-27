from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='fotos_perfil/', blank=True, null=True)
    curso = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"Perfil de {self.user.username}"


class Habilidade(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='habilidades')
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Competencia(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='competencias')
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
    


class PaginaFrontend(models.Model):
    titulo_principal = models.CharField(max_length=200)
    descricao_principal = models.TextField(blank=True, null=True, verbose_name="Descrição Principal")
    motivo_escolher = models.TextField(blank=True, null=True, verbose_name="Motivos para Escolher Backend")
    faixa_junior = models.CharField(max_length=50, default="R$ 4.500", verbose_name="Faixa Salarial Júnior")
    faixa_pleno = models.CharField(max_length=50, default="R$ 9.500", verbose_name="Faixa Salarial Pleno")
    faixa_senior = models.CharField(max_length=50, default="R$ 18.000", verbose_name="Faixa Salarial Sênior")
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Página Frontend"

class PaginaBackend(models.Model):
    titulo_principal = models.CharField(max_length=200, default="Por Que Estudar Backend?", verbose_name="Título Principal")
    descricao_principal = models.TextField(blank=True, null=True, verbose_name="Descrição Principal")
    motivo_escolher = models.TextField(blank=True, null=True, verbose_name="Motivos para Escolher Backend")
    faixa_junior = models.CharField(max_length=50, default="R$ 4.500", verbose_name="Faixa Salarial Júnior")
    faixa_pleno = models.CharField(max_length=50, default="R$ 7.500", verbose_name="Faixa Salarial Pleno")
    faixa_senior = models.CharField(max_length=50, default="R$ 15.000", verbose_name="Faixa Salarial Sênior")
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Página Backend"
    

class PaginaMobile(models.Model):
    titulo_principal = models.CharField(max_length=200, default="Por Que Estudar Backend?", verbose_name="Título Principal")
    descricao_principal = models.TextField(blank=True, null=True, verbose_name="Descrição Principal")
    motivo_escolher = models.TextField(blank=True, null=True, verbose_name="Motivos para Escolher Backend")
    faixa_junior = models.CharField(max_length=50, default="R$ 4.500", verbose_name="Faixa Salarial Júnior")
    faixa_pleno = models.CharField(max_length=50, default="R$ 9.500", verbose_name="Faixa Salarial Pleno")
    faixa_senior = models.CharField(max_length=50, default="R$ 18.000", verbose_name="Faixa Salarial Sênior")
    atualizado_em = models.DateTimeField(auto_now=True)


    def __str__(self):
        return "Página Mobile"

class PaginaCiencia(models.Model):
    titulo_principal = models.CharField(max_length=200, default="Por Que Estudar Ciência de Dados?", verbose_name="Título Principal")
    descricao_principal = models.TextField(blank=True, null=True, verbose_name="Descrição Principal")
    motivo_escolher = models.TextField(blank=True, null=True, verbose_name="Motivos para Escolher Backend")
    faixa_junior = models.CharField(max_length=50, default="R$ 6.000", verbose_name="Faixa Salarial Júnior")
    faixa_pleno = models.CharField(max_length=50, default="R$ 12.000", verbose_name="Faixa Salarial Pleno")
    faixa_senior = models.CharField(max_length=50, default="R$ 25.000", verbose_name="Faixa Salarial Sênior")
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Página Ciência de Dados"


class PaginaEngenharia(models.Model):
    titulo_principal = models.CharField(max_length=200, default="Por Que Estudar Engenharia de Dados?", verbose_name="Título Principal")
    descricao_principal = models.TextField(blank=True, null=True, verbose_name="Descrição Principal")
    motivo_escolher = models.TextField(blank=True, null=True, verbose_name="Motivos para Escolher Engenharia de Dados")
    faixa_junior = models.CharField(max_length=50, default="R$ 7.000", verbose_name="Faixa Salarial Júnior")
    faixa_pleno = models.CharField(max_length=50, default="R$ 14.000", verbose_name="Faixa Salarial Pleno")
    faixa_senior = models.CharField(max_length=50, default="R$ 22.000", verbose_name="Faixa Salarial Sênior")
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Página Engenharia de Dados"
    

class PaginaAnalistaBI(models.Model):
    titulo_principal = models.CharField(max_length=200, default="Por Que Estudar Business Intelligence ?", verbose_name="Título Principal")
    descricao_principal = models.TextField(blank=True, null=True, verbose_name="Descrição Principal")
    motivo_escolher = models.TextField(blank=True, null=True, verbose_name="Motivos para Escolher Analista de BI")
    faixa_junior = models.CharField(max_length=50, default="R$ 4.500", verbose_name="Faixa Salarial Júnior")
    faixa_pleno = models.CharField(max_length=50, default="R$ 7.000", verbose_name="Faixa Salarial Pleno")
    faixa_senior = models.CharField(max_length=50, default="R$ 15.000", verbose_name="Faixa Salarial Sênior")
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Página Analista de BI"
    

class PaginaAnaliseSeguranca(models.Model):
    titulo_principal = models.CharField(max_length=200, default="Por Que Estudar Análise de Segurança?", verbose_name="Título Principal")
    descricao_principal = models.TextField(blank=True, null=True, verbose_name="Descrição Principal")
    motivo_escolher = models.TextField(blank=True, null=True, verbose_name="Motivos para Escolher Análise de Dados")
    faixa_junior = models.CharField(max_length=50, default="R$ 3.000", verbose_name="Faixa Salarial Júnior")
    faixa_pleno = models.CharField(max_length=50, default="R$ 5.500", verbose_name="Faixa Salarial Pleno")
    faixa_senior = models.CharField(max_length=50, default="R$ 16.000", verbose_name="Faixa Salarial Sênior")
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Página Análise de Dados"
    
class PaginaForense(models.Model):
    titulo_principal = models.CharField(max_length=200, default="Por Que Estudar a Area de Forense Digital?", verbose_name="Título Principal")
    descricao_principal = models.TextField(blank=True, null=True, verbose_name="Descrição Principal")
    motivo_escolher = models.TextField(blank=True, null=True, verbose_name="Motivos para Escolher Forense Digital")
    faixa_junior = models.CharField(max_length=50, default="R$ 3.500", verbose_name="Faixa Salarial Júnior")
    faixa_pleno = models.CharField(max_length=50, default="R$ 6.500", verbose_name="Faixa Salarial Pleno")
    faixa_senior = models.CharField(max_length=50, default="R$ 20.000", verbose_name="Faixa Salarial Sênior")
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Página Forense Digital"
    
class PaginaEngenhariaSeguranca(models.Model):
    titulo_principal = models.CharField(max_length=200, default="Por Que Estudar a Área de Engenharia de Segurança?", verbose_name="Título Principal")
    descricao_principal = models.TextField(blank=True, null=True, verbose_name="Descrição Principal")
    motivo_escolher = models.TextField(blank=True, null=True, verbose_name="Motivos para Escolher Engenharia de Segurança")
    faixa_junior = models.CharField(max_length=50, default="R$ 4.000", verbose_name="Faixa Salarial Júnior")
    faixa_pleno = models.CharField(max_length=50, default="R$ 8.000", verbose_name="Faixa Salarial Pleno")
    faixa_senior = models.CharField(max_length=50, default="R$ 18.000", verbose_name="Faixa Salarial Sênior")
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Página Engenharia de Segurança"
    
class PaginaAdmRedes(models.Model):
    titulo_principal = models.CharField(max_length=200, default="Por Que Estudar Administração de Redes?", verbose_name="Título Principal")
    descricao_principal = models.TextField(blank=True, null=True, verbose_name="Descrição Principal")
    motivo_escolher = models.TextField(blank=True, null=True, verbose_name="Motivos para Escolher Administração de Redes")
    faixa_junior = models.CharField(max_length=50, default="R$ 5.500", verbose_name="Faixa Salarial Júnior")
    faixa_pleno = models.CharField(max_length=50, default="R$ 8.500", verbose_name="Faixa Salarial Pleno")
    faixa_senior = models.CharField(max_length=50, default="R$ 15.000", verbose_name="Faixa Salarial Sênior")
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Página Administração de Redes"
    
class Categoria(models.Model):
    nome = models.CharField(max_length=100, unique=True, verbose_name="Nome da Categoria")
    ordem = models.PositiveIntegerField(default=0, help_text="Use para definir a ordem na página (ex: 1, 2, 3...)")

    class Meta:
        verbose_name = "Categoria de Carreira"
        verbose_name_plural = "1. Categorias de Carreiras" 
        ordering = ['ordem', 'nome']
    
    def __str__(self):
        return self.nome

class Carreira(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='carreiras', verbose_name="Categoria")
    titulo = models.CharField(max_length=100, verbose_name="Título do Card")
    descricao = models.TextField(verbose_name="Descrição Curta")
    url_nome = models.CharField(
        max_length=100, 
        verbose_name="Nome da URL (para o botão 'Saiba Mais')",
        help_text="Ex: 'pagina_front'. Use '#' se não tiver uma página de detalhe."
    )
    ordem = models.PositiveIntegerField(default=0, help_text="Use para definir a ordem dos cards (ex: 1, 2, 3...)")

    class Meta:
        verbose_name = "Carreira"
        verbose_name_plural = "2. Carreiras"
        ordering = ['categoria__ordem', 'ordem', 'titulo']

    def __str__(self):
        return f"{self.categoria.nome} - {self.titulo}"
    
class Projeto(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projetos')
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    # imagem = models.ImageField(upload_to='fotos_projetos/', blank=True, null=True, help_text="Opcional: Imagem de capa do projeto.")
    link_repositorio = models.URLField(max_length=200, blank=True, null=True, verbose_name="Link do Repositório (Ex: GitHub)")
    link_producao = models.URLField(max_length=200, blank=True, null=True, verbose_name="Link da Aplicação (Opcional)")
    
    class Meta:
        verbose_name = "Projeto"
        verbose_name_plural = "Projetos"
        ordering = ['-id'] 

    def __str__(self):
        return self.titulo