from django.contrib import messages
from django.views.generic import TemplateView
from django.utils.translation import gettext as _

from aplic.forms import ContatoForm
from aplic.models import Professor


class IndexView(TemplateView):
    template_name = 'index.html'
    form_class = ContatoForm
    success_url = reversed('index')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['professores'] = Professor.objects.order_by('nome').all()
        return context

    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.success(self.request, _('E-mail enviado com sucesso'), extra_tags='success')
        return super(IndexView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, _('Falha ao enviar e-mail'), extra_tags='danger')
        return super(IndexView, self).form_invalid(form, *args, **kwargs)

