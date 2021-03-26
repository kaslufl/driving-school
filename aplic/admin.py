from django.contrib import admin
from .models import Aluno, Professor, Conteudo, Turma, Veiculo, AulaPratica, AulaTeorica


@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'matricula', 'cnh', 'situacao', 'categoria', 'esta_ativo')


@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'matricula', 'cnh', 'especializacao', 'esta_ativo')


@admin.register(Conteudo)
class ConteudoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'carga_horaria')


@admin.register(Turma)
class TurmaAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'max_aluno', 'conteudo', 'professor')


@admin.register(Veiculo)
class VeiculoAdmin(admin.ModelAdmin):
    list_display = ('placa', 'modelo', 'categoria', 'esta_apto')


@admin.register(AulaPratica)
class AulaPraticaAdmin(admin.ModelAdmin):
    list_display = ('data', 'aluno', 'professor', 'veiculo')


@admin.register(AulaTeorica)
class AulaTeoricaAdmin(admin.ModelAdmin):
    list_display = ('data', 'turma', 'professor')
