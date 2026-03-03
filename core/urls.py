from django.urls import path
from .views import IndexView, DadosJSONView, GraficoPDFView 

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('dados/', DadosJSONView.as_view(), name='dados'),
    path('gerar-pdf/', GraficoPDFView.as_view(), name='gerar_pdf'),
]







