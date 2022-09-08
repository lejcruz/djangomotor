from django.db import models
from django import forms

# Create your models here.
class Ancora(models.Model):
    name = models.CharField(max_length=30)
    valor_cpf_cnpj = models.CharField(max_length=18)

    def __str__(self):
        return f'{self.name} - {self.valor_cpf_cnpj}'