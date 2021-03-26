from django.contrib import admin
from .models import Aluno, Professor, Conteudo, Turma


@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'matricula', 'cnh', 'situacao', 'categoria')


@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'matricula', 'cnh', 'especializacao')


@admin.register(Conteudo)
class ConteudoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'carga_horaria')


@admin.register(Turma)
class TurmaAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'max_aluno', 'conteudo', 'professor')
