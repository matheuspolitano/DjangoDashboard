from django.contrib import admin
from .models import  DadosEmpresa


@admin.register(DadosEmpresa)

class ModelAdmin(admin.ModelAdmin):
    list_display = ["mes","ano_2018","ano_2019"]
# Register your models here.
