from django.db import models
from pacientes.models import Paciente

class Evolucao(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    data_sessao = models.DateField()
    observacoes = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Evolução de {self.paciente.nome} em {self.data_sessao}"