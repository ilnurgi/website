# coding: utf-8

from django.views.generic import TemplateView

from application.views import IsSuperUserMixin


class BlogHomePage(IsSuperUserMixin, TemplateView):

    template_name = 'blog_index.html'

    def get_context_data(self, **kwargs):
        context = super(BlogHomePage, self).get_context_data(**kwargs)
        context['active_page'] = 'blog'
        return context
