from django.db import models
from django import forms


# Create your models here.
class Produtor(models.Model):
    name = models.CharField(max_length=30)
    valor_cpf_cnpj = models.CharField(max_length=18)
    municipio = models.CharField(max_length=50)
    estado = models.CharField(max_length=2)


    def __str__(self):
        return f'{self.name} - {self.valor_cpf_cnpj} - {self.municipio}/{self.estado}'


class ProdutorCultura(models.Model):
    produtor = models.ForeignKey(Produtor, on_delete=models.CASCADE)

    cultura = models.CharField(max_length=30)
    area = models.IntegerField()

    def __str__(self):
        return f'{self.produtor} - {self.cultura} - {self.area}'
        