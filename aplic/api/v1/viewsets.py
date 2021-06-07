from aplic.models import (Aluno, AulaPratica, AulaTeorica, Conteudo, Endereco,
                          Professor, Turma, Veiculo)
from rest_framework import viewsets, permissions

from .serializers import (AlunoSerializer, AulaPraticaSerializer,
                          AulaTeoricaSerializer, ConteudoSerializer,
                          EnderecoSerializer, ProfessorSerializer,
                          TurmaSerializer, VeiculoSerializer)

class AlunoViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.DjangoModelPermissions, )
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer


class AulaPraticaViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.DjangoModelPermissions, )
    queryset = AulaPratica.objects.all()
    serializer_class = AulaPraticaSerializer


class AulaTeoricaViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.DjangoModelPermissions, )
    queryset = AulaTeorica.objects.all()
    serializer_class = AulaTeoricaSerializer


class ConteudoViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.DjangoModelPermissions, )
    queryset = Conteudo.objects.all()
    serializer_class = ConteudoSerializer


class EnderecoViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.DjangoModelPermissions, )
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer


class ProfessorViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.DjangoModelPermissions, )
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer


class TurmaViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.DjangoModelPermissions, )
    queryset = Turma.objects.all()
    serializer_class = TurmaSerializer


class VeiculoViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.DjangoModelPermissions, )
    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer
