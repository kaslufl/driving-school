from django.contrib import admin

# Register your models here.
@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'endereco', 'matricula', 'cnh', 'digital', 'tipo')


@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'endereco', 'matricula', 'cnh', 'digital', 'tipo', 'tipo_cnh', 'estado')


@admin.register(Turma)
class TurmaAdmin(admin.ModelAdmin):
    list_display = ('max_alunos')