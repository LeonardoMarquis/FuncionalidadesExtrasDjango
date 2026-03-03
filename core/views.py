from django.shortcuts import render

from random import randint

from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView


class IndexView(TemplateView):
    template_name = 'index.html'

class DadosJSONView(BaseLineChartView):

    def get_labels(self):
        """Retorna os meses do ano como labels"""
        labels = [
                "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", 
                "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
        ]

        return labels

    def get_providers(self):
        # retorna os nomes das linhas do grafico, datasets
        # datasets serao os produtos mais vendidos
        datasets = [
            "Peito de Frango","Coca-cola",
            "Arroz", "Feijão Preto",
            "Sal", "Leite","Ovos",
            "Pão", "Queijo", "Iogurte", "Manteiga",
            "Café", "Açúcar","Macarrão", "Óleo de Milho",
        ]

        return datasets

    def get_data(self):
        # retorna os datasets para plotar o grafico

        dados = []

        for produto in range(15):
            
            valores_produto = []
            for mes in range(12):
                valores_produto.append(randint(1, 200))
            dados.append(valores_produto)


        return dados





