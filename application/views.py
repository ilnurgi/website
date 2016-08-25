# coding: utf-8

from django.views.generic import TemplateView

from application.constants import CONSPECTS
from blog.models import Category


class ConspectsMixin(object):

    def get_context_data(self, **kwargs):
        context = super(ConspectsMixin, self).get_context_data(**kwargs)
        context['conspects'] = CONSPECTS
        return context


class SiteMap(ConspectsMixin, TemplateView):
    template_name = 'application/sitemap.html'

    def get_context_data(self, **kwargs):
        context = super(SiteMap, self).get_context_data(**kwargs)

        context['active_page'] = 'sitemap'

        categories = Category.objects
        if not self.request.user.is_superuser:
            categories = categories.filter(post__published=True)
        context['categories'] = categories.all()
        return context


class ConspectsPage(ConspectsMixin, TemplateView):
    template_name = 'application/conspects.html'
