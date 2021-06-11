from django.urls import path, include
from .api.v1.router import router as v1
from .views import IndexView, ContatoView, DadosGraficoTurmaView, RelatorioAlunosView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('conato/', ContatoView.as_view(), name='contato'),
    path('api/v1/', include(v1.urls)),
    path('api/v1/api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('dados-grafico-turma/', DadosGraficoTurmaView.as_view(), name='dados-grafico-turma'),
    path('relatorio-alunos/', RelatorioAlunosView.as_view(), name='relatorio-alunos'),
]
