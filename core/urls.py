from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import IndexView, DadosJSONView, GraficoPDFView, HomeView, LoginView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('dados/', DadosJSONView.as_view(), name='dados'),
    path('gerar-pdf/', GraficoPDFView.as_view(), name='gerar_pdf'),

    path('home/', HomeView.as_view(), name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'), # vamos usar a do proprio django, entao nao precisa criar ela
    path('social-auth/', include('social_django.urls', namespace='social')),    # para permitir fazer login com as redes socias
    path('', IndexView.as_view(), name='index'),    # para se nao estiver logado e  tentar acessar a pagina home, manda rpara a de fazer login
]







