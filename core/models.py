from django.db import models

# Create your models here.



class DadosEmpresa(models.Model):
    mes = models.CharField("Mes",max_length=100)
    ano_2018 = models.CharField("Ano 2018",max_length=100)
    ano_2019 = models.CharField("Ano 2019",max_length=100)

