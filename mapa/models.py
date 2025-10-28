from django.db import models


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
