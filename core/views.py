from django.shortcuts import render
from django.views.generic import TemplateView
from .models import DadosEmpresa



# Create your views here.
class MyView(TemplateView):
    template_name = "index.htm"

    mes = []
    ano_2018 = []
    ano_2019 = []

    for item in DadosEmpresa.objects.all():
        mes.append(item.mes)
        ano_2018.append(item.ano_2018)
        ano_2019.append(item.ano_2019)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["mes"] = self.mes
        context["ano_2018"]= self.ano_2018
        context["ano_2019"] = self.ano_2019
        return context
