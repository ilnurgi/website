# coding: utf-8

from django.conf import settings
from django.views.generic import TemplateView


class HomePage(TemplateView):
    template_name = 'resume.html'

    def get_context_data(self, **kwargs):
        context = super(HomePage, self).get_context_data(**kwargs)
        context['GOOGLE_SITE_VERIFICATIN'] = settings.GOOGLE_SITE_VERIFICATIN
        return context
