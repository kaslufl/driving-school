from aplic.models import (Aluno, AulaPratica, AulaTeorica, Conteudo, Endereco,
                          Professor, Turma, Veiculo)
from rest_framework import serializers


class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = '__all__'


class AulaPraticaSerializer(serializers.ModelSerializer):
    class Meta:
        model = AulaPratica
        fields = '__all__'


class AulaTeoricaSerializer(serializers.ModelSerializer):
    class Meta:
        model = AulaTeorica
        fields = '__all__'


class ConteudoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conteudo
        fields = '__all__'


class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = '__all__'


class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = '__all__'


class TurmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turma
        fields = '__all__'


class VeiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Veiculo
        fields = '__all__'
