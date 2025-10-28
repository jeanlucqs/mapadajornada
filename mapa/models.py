from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='fotos_perfil/', blank=True, null=True)
    curso = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"Perfil de {self.user.username}"

# Modelos opcionais separados — se preferir armazenar cada item em tabela separada
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
    introducao = models.TextField()
    motivo_escolher = models.TextField()
    publico_alvo = models.TextField()
    conteudo_aprendizado = models.TextField()
    profissoes = models.TextField()

    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Página Frontend"

class PaginaBackend(models.Model):
    titulo_principal = models.CharField(max_length=200, default="Por Que Estudar Backend?", verbose_name="Título Principal")
    descricao_principal = models.TextField(blank=True, null=True, verbose_name="Descrição Principal")
    motivo_escolher = models.TextField(blank=True, null=True, verbose_name="Motivos para Escolher Backend")
    faixa_junior = models.CharField(max_length=50, default="R$ 4.500", verbose_name="Faixa Salarial Júnior")
    faixa_pleno = models.CharField(max_length=50, default="R$ 9.500", verbose_name="Faixa Salarial Pleno")
    faixa_senior = models.CharField(max_length=50, default="R$ 18.000", verbose_name="Faixa Salarial Sênior")

    def __str__(self):
        return "Página Backend"
    

class PaginaMobile(models.Model):
    titulo_principal = models.CharField(max_length=200, default="Por Que Estudar Backend?", verbose_name="Título Principal")
    descricao_principal = models.TextField(blank=True, null=True, verbose_name="Descrição Principal")
    motivo_escolher = models.TextField(blank=True, null=True, verbose_name="Motivos para Escolher Backend")
    faixa_junior = models.CharField(max_length=50, default="R$ 4.500", verbose_name="Faixa Salarial Júnior")
    faixa_pleno = models.CharField(max_length=50, default="R$ 9.500", verbose_name="Faixa Salarial Pleno")
    faixa_senior = models.CharField(max_length=50, default="R$ 18.000", verbose_name="Faixa Salarial Sênior")


    def __str__(self):
        return "Página Mobile"
