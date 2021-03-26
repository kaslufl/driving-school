from django.db import models


class Pessoa(models.Model):
    OPCOES_CNH = (
        ('Não possui', 'Não possui'),
        ('Categoria A', 'Categoria A'),
        ('Categoria B', 'Categoria B'),
        ('Categoria C', 'Categoria C'),
        ('Categoria D', 'Categoria D'),
        ('Categoria E', 'Categoria E'),
        ('ACC', 'ACC'),
    )
    nome = models.CharField('Nome', max_length=100)
    data_nascimento = models.DateField('Data de Nascimento', help_text='Formato DD/MM/AAAA')
    cpf = models.CharField('CPF', max_length=15)
    endereco = models.CharField('Endereço', max_length=100)
    matricula = models.IntegerField('Matrícula', unique=True)
    cnh = models.CharField('CNH', max_length=20, choices=OPCOES_CNH)

    class Meta:
        abstract = True

    def __str__(self):
        return self.nome


class Aluno(Pessoa):
    OPCOES_SITUACAO = (
        ('1ª Habilitação', '1ª Habilitação'),
        ('Renovação', 'Renovação'),
        ('CRCI', 'CRCI'),
    )
    OPCOES_CATEGORIA = (
        ('Categoria A', 'Categoria A'),
        ('Categoria B', 'Categoria B'),
        ('Categoria C', 'Categoria C'),
        ('Categoria D', 'Categoria D'),
        ('Categoria E', 'Categoria E'),
        ('ACC', 'ACC'),
    )

    situacao = models.CharField('Situação da Carteira',
                                max_length=20,
                                choices=OPCOES_SITUACAO)

    categoria = models.CharField('Categoria',
                                 max_length=20,
                                 choices=OPCOES_CATEGORIA)

    class Meta:
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'


class Professor(Pessoa):
    OPCOES_ESPECIALIZACAO = (
        ('Instrutor Prático', 'Instrutor Prático'),
        ('Instrutor Teórico', 'Instrutor Teórico'),
    )
    especializacao = models.CharField('Especialização',
                                      max_length=20,
                                      choices=OPCOES_ESPECIALIZACAO)

    class Meta:
        verbose_name = 'Professor'
        verbose_name_plural = 'Professores'


class Conteudo(models.Model):
    nome = models.CharField('Nome', max_length=100)
    descricao = models.TextField('Descrição', max_length=500)
    carga_horaria = models.IntegerField('Carga Horária')

    class Meta:
        verbose_name = 'Conteúdo'
        verbose_name_plural = 'Conteúdos'

    def __str__(self):
        return self.nome


class Turma(models.Model):
    codigo = models.CharField('Código', max_length=10)
    max_aluno = models.IntegerField('Quantidade de alunos por turma')
    professor = models.ForeignKey(Professor, null=True, on_delete=models.SET_NULL)
    conteudo = models.ForeignKey(Conteudo, on_delete=models.CASCADE)
    alunos = models.ManyToManyField(Aluno)

    class Meta:
        verbose_name = 'Turma'
        verbose_name_plural = 'Turmas'

    def __str__(self):
        return f"{self.codigo} - {self.conteudo} - {self.max_aluno}"
