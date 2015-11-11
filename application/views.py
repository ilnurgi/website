# coding: utf-8

from django.views.generic import TemplateView


class HomePage(TemplateView):

    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(HomePage, self).get_context_data(**kwargs)

        context['active_page'] = 'main'

        return context

