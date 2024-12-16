from django.db import models

class Funcionario(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    cpf = models.CharField(max_length=11, null=False, blank=False)  # CPF
    remuneracao = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)  # Remuneração
    