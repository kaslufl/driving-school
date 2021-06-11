from django.db import models
from stdimage.models import StdImageField
import uuid
from django.utils.translation import gettext_lazy as _


def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename


OPCOES_CATEGORIA = (
        ('Categoria A', _('Categoria A')),
        ('Categoria B', _('Categoria B')),
        ('Categoria C', _('Categoria C')),
        ('Categoria D', _('Categoria D')),
        ('Categoria E', _('Categoria E')),
        ('ACC', _('ACC')),
    )

class Estado(models.Model):
    uf = models.CharField(_('UF'), max_length=2, unique=True)
    nome = models.CharField(_('Estado'), max_length=55)

    class Meta:
        verbose_name = _('Estado')
        verbose_name_plural = _('Estados')
        ordering = ['id']

    def __str__(self):
        return f'{self.uf} - {self.nome}'


class Cidade(models.Model):
    nome = models.CharField(_('Cidade'), max_length=255)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('Cidade')
        verbose_name_plural = _('Cidades')
        ordering = ['id']

    def __str__(self):
        return f'{self.nome}'


class Logradouro(models.Model):
    nome = models.CharField(_('Rua'), max_length=255)
    cep = models.CharField(_('CEP'), max_length=8)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('Logradouro')
        verbose_name_plural = _('Logradouros')
        ordering = ['id']

    def __str__(self):
        return f'{self.nome}'


class Endereco(models.Model):
    logradouro = models.ForeignKey(Logradouro, on_delete=models.DO_NOTHING)
    complemento = models.CharField(_('Complemento'), blank=True, max_length=255)
    numero = models.CharField(_('Número'), max_length=9)

    class Meta:
        verbose_name = _('Endereço')
        verbose_name_plural = _('Endereços')
        ordering = ['id']

    def __str__(self):
        return f'{self.logradouro}'


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
    nome = models.CharField(_('Nome'), max_length=100)
    data_nascimento = models.DateField(_('Data de Nascimento'), help_text='Formato DD/MM/AAAA')
    cpf = models.CharField(_('CPF'), max_length=15)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)
    matricula = models.IntegerField(_('Matrícula'), unique=True)
    cnh = models.CharField(_('CNH'), max_length=20, choices=OPCOES_CNH)

    class Meta:
        abstract = True

    def __str__(self):
        return self.nome


class Aluno(Pessoa):
    OPCOES_SITUACAO = (
        ('1ª Habilitação', _('1ª Habilitação')),
        ('Renovação', _('Renovação')),
        ('CRCI', _('CRCI')),
    )
    esta_ativo = models.BooleanField(_('Aluno em Atividade'), default=True)
    situacao = models.CharField(_('Situação da Carteira'),
                                max_length=20,
                                choices=OPCOES_SITUACAO)

    categoria = models.CharField(_('Categoria'),
                                 max_length=20,
                                 choices=OPCOES_CATEGORIA)

    class Meta:
        verbose_name = _('Aluno')
        verbose_name_plural = _('Alunos')


class Professor(Pessoa):
    OPCOES_ESPECIALIZACAO = (
        ('Instrutor Prático', _('Instrutor Prático')),
        ('Instrutor Teórico', _('Instrutor Teórico')),
    )
    esta_ativo = models.BooleanField(_('Professor em Atividade'), default=True)
    especializacao = models.CharField(_('Especialização'),
                                      max_length=20,
                                      choices=OPCOES_ESPECIALIZACAO)
    facebook = models.CharField('Facebook', blank=True, max_length=200)
    linkedin = models.CharField('Linkedin', blank=True, max_length=200)
    twitter = models.CharField('Twitter', blank=True, max_length=200)
    instagram = models.CharField('Instagram', blank=True, max_length=200)
    foto = StdImageField(_('Foto'), null=True, blank=True, upload_to=get_file_path, variations={'thumb': {'width': 480, 'height': 480, 'crop': True}})

    class Meta:
        verbose_name = _('Professor')
        verbose_name_plural = _('Professores')


class Conteudo(models.Model):
    nome = models.CharField(_('Nome'), max_length=100)
    descricao = models.TextField(_('Descrição'), max_length=500)
    carga_horaria = models.IntegerField(_('Carga Horária'))

    class Meta:
        verbose_name = _('Conteúdo')
        verbose_name_plural = _('Conteúdos')

    def __str__(self):
        return self.nome


class Turma(models.Model):
    codigo = models.CharField(_('Código'), max_length=10)
    max_aluno = models.IntegerField(_('Quantidade de alunos max de alunos'))
    professor = models.ForeignKey(Professor,
                                  null=True,
                                  on_delete=models.SET_NULL)
    conteudo = models.ForeignKey(Conteudo, on_delete=models.CASCADE)
    alunos = models.ManyToManyField(Aluno)

    class Meta:
        verbose_name = _('Turma')
        verbose_name_plural = _('Turmas')

    def __str__(self):
        return f"{self.codigo} - {self.conteudo} - {self.max_aluno}"


class Veiculo(models.Model):
    placa = models.CharField(_('Placa'), max_length=7)
    modelo = models.CharField(_('Modelo'), max_length=100)
    esta_apto = models.BooleanField(_('Apto para Uso'), default=True)
    categoria = models.CharField(_('Categoria'),
                                 max_length=20,
                                 choices=OPCOES_CATEGORIA)

    class Meta:
        verbose_name = _('Veículo')
        verbose_name_plural = _('Veículos')

    def __str__(self):
        return f"{self.placa} - {self.modelo} - {self.categoria}"


class Aula(models.Model):
    data = models.DateField(_('Data'), help_text='Formato DD/MM/AAAA')
    duracao = models.IntegerField(_('Duração'), help_text='Quantidade de Horas')
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class AulaPratica(Aula):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('Aula Prática')
        verbose_name_plural = _('Aulas Práticas')

    def __str__(self):
        return f"{self.data} - {self.aluno} - {self.professor} - {self.veiculo}"


class AulaTeorica(Aula):
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('Aula Teórica')
        verbose_name_plural = _('Aulas Teóricas')

    def __str__(self):
        return f"{self.data} - {self.turma} - {self.professor}"
