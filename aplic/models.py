from django.db import models

class Pessoa(models.Model):
    OPCOES1 = (
        ('Possui', 'Possui')
        ('Não possui', 'Não possui')
    )
    nome = models.CharField('Nome', max_length=100)
    cpf = models.CharField('CPF', max_length=15)
    endereco = models.CharField('Endereço', max_length=100)
    matricula = models.IntegerField('Matricula', unique=True)
    cnh = models.CharField('CNH', max_length=20, choices=OPCOES1)
    digital = models.CharField('Digital', max_length=20, choices=OPCOES1)

    class Meta:
        abstract = True

    def __str__(self):
        return self.nome

class Aluno(Pessoa):
    OPCOESCNH = (
        ('Tipo A', 'Tipo A')
        ('Tipo B', 'Tipo B')
        ('Tipo C', 'Tipo C')
    )

    #ESTADO = () verificar o estado que o aluno ira possuir

    tipo_cnh = models.CharField('Tipo de CNH', max_length=20, choices=OPCOESCNH)
    estado = models.CharField("Estado", max_length=20)

    class Meta:
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'

class Professor(Pessoa):

    #TIPO = () verificar o tipo que o professor ira possuir

    tipo = models.CharField("Tipo", max_length=20)

    class Meta:
        verbose_name = 'Professor'
        verbose_name_plural = 'Professores'

class Turma(models.Model):

    max_aluno = models.IntegerField('Quantidade de alunos por turma')
    professor = models.ForeignKey(Professor, null=True, on_delete=models.SET_NULL)
    alunos = models.ManyToManyField(Aluno)

    class Meta:
        verbose_name = 'Turma'
        verbose_name_plural = 'Turmas'
