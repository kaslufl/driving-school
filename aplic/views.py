from django.views.generic import TemplateView
from aplic.models import Professor


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['professores'] = Professor.objects.order_by('nome').all()
        return context