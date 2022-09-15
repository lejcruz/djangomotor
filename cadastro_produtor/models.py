from django.db import models
from django import forms
from django.core import validators
from pyUFbr.baseuf import ufbr




# Create your models here.

VALIDATOR_FOR_AREA = [validators.MaxValueValidator(12000,"Área Máxima Permitida é de 12mil hectares"), 
                      validators.MinValueValidator(1,"Área Mínima Permitida é de 1 hectare")
                     ]


CULTURA_CHOICES= [
    ('soja', 'Soja'),
    ('milho', 'Milho'),
    ('café', 'Café'),
    ('algodao', 'Algodao'),
    ]


ESTADO_CHOICES= [(uf, uf) for uf in ufbr.list_uf]

# POr enquanto vou deixar sem a opção de escolher a cidade e colocar essa feature depois

class Produtor(models.Model):
    name = models.CharField(max_length=30)
    cpf_cnpj = models.CharField(max_length=18)
    municipio = models.CharField(max_length=50)
    estado = models.CharField(max_length=2, choices=ESTADO_CHOICES, default=None)

    cultura1 = models.CharField(max_length=30, choices=CULTURA_CHOICES, null=True, blank=True)
    area1 = models.IntegerField(validators=VALIDATOR_FOR_AREA, null=True, blank=True)

    cultura2 = models.CharField(max_length=30, choices=CULTURA_CHOICES, null=True, blank=True)
    area2 = models.IntegerField(validators=VALIDATOR_FOR_AREA, null=True, blank=True)

    cultura3 = models.CharField(max_length=30, choices=CULTURA_CHOICES, null=True, blank=True)
    area3 = models.IntegerField(validators=VALIDATOR_FOR_AREA, null=True, blank=True)

    cultura4 = models.CharField(max_length=30, choices=CULTURA_CHOICES, null=True, blank=True)
    area4 = models.IntegerField(validators=VALIDATOR_FOR_AREA, null=True, blank=True)


    def __str__(self):
        return f"""
        {self.name} - {self.cpf_cnpj} - {self.municipio}/{self.estado} 
        [{self.cultura1}:{self.area1}, 
        {self.cultura2}:{self.area2},
        {self.cultura3}:{self.area3},
        {self.cultura4}:{self.area4},
        ]"""

        