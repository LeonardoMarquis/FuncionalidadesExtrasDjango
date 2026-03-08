from django.shortcuts import render

from random import randint

from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView


class IndexView(TemplateView):
    template_name = 'index.html'

class DadosJSONView(BaseLineChartView):

    def get_labels(self):
        # meses do ano
        labels = [
                "Janeiro", "Fevereiro", "Março", "Abril",   "Maio", "Junho", 
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


# View para gerar o PDF

from django.http import HttpResponse
from django.views.generic import View
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.linecharts import HorizontalLineChart
import io

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

class GraficoPDFView(View):

    def get(self, request):

        
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="Relatorio_simples.pdf"'
        
        p = canvas.Canvas(response, pagesize=A4)
        p.setTitle("Relatório Simples")
        
        # titulo
        p.setFont("Helvetica-Bold", 16)
        p.drawString(50, 800, "Relatório de Vendas - Resumo")
        
        # lista de produtos

        p.setFont("Helvetica", 12)
        y = 750
        produtos = [
            "Peito de Frango","Coca-cola",
            "Arroz", "Feijão Preto",
            "Sal", "Leite","Ovos",
            "Pão", "Queijo", "Iogurte", "Manteiga",
            "Café", "Açúcar","Macarrão", "Óleo de Milho",
        ]
        
        for produto in produtos:
            total = randint(0, 2400)
            p.drawString(50, y, f"{produto}: {total} unidades")
            y -= 20
        
        p.showPage()
        p.save()
        
        return response

