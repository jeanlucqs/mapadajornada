from django.db import models
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

