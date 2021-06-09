from chartjs.views.lines import BaseLineChartView
from django.contrib import messages
from django.db.models import Count
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import FormView, TemplateView

from aplic.forms import ContatoForm
from aplic.models import Professor, Turma


class IndexView(TemplateView):
    template_name = 'index.html'
    form_class = ContatoForm
    success_url = reversed('index')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['professores'] = Professor.objects.order_by('nome').all()
        return context


class ContatoView(FormView):
    template_name = 'contato.html'
    form_class = ContatoForm
    success_url = reverse_lazy('contato')

    def get_context_data(self, **kwargs):
        context = super(ContatoView, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.success(self.request, _('E-mail enviado com sucesso'), extra_tags='success')
        return super(ContatoView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, _('Falha ao enviar e-mail'), extra_tags='danger')
        return super(ContatoView, self).form_invalid(form, *args, **kwargs)


class DadosGraficoTurmaView(BaseLineChartView):

    def get_labels(self):
        labels = []
        queryset = Turma.objects.order_by('id').aggregate()
        for turma in queryset:
            labels.append(turma.codigo)
        return labels

    def get_data(self):
        resultado = []
        dados = []
        queryset = Turma.objects.order_by('id').annotate(total=Count('alunos'))
        for linha in queryset:
            dados.append(int(linha.total))
        resultado.append(dados)
        return resultado
