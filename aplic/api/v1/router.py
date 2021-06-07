from rest_framework import routers

from .viewsets import (AlunoViewSet, AulaPraticaViewSet, AulaTeoricaViewSet,
                       ConteudoViewSet, EnderecoViewSet, ProfessorViewSet,
                       TurmaViewSet, VeiculoViewSet)

router = routers.DefaultRouter()
router.register(r'alunos', AlunoViewSet)
router.register(r'aulas-praticas', AulaPraticaViewSet)
router.register(r'aluas-teoricas', AulaTeoricaViewSet)
router.register(r'conteudos', ConteudoViewSet)
router.register(r'enderecos', EnderecoViewSet)
router.register(r'professores', ProfessorViewSet)
router.register(r'turmas', TurmaViewSet)
router.register(r'veiculos', VeiculoViewSet)
