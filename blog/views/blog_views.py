# coding: utf-8

from django.views.generic import TemplateView

from application.views import IsSuperUserMixin
from blog.models import Tags, Post


class BaseBlogViewMixin(object):

    def get_context_data(self, **kwargs):
        context = super(BaseBlogViewMixin, self).get_context_data(**kwargs)
        context['active_page'] = 'blog'
        context['tags'] = list(Tags.objects.all())
        return context


class HomePage(BaseBlogViewMixin, IsSuperUserMixin, TemplateView):

    template_name = 'blog_index.html'

    def get_context_data(self, **kwargs):
        context = super(HomePage, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        return context


class TagPage(HomePage):

    def get_context_data(self, **kwargs):
        context = super(HomePage, self).get_context_data(**kwargs)
        context['current_tag_id'] = self.kwargs['tag_id']
        context['posts'] = Post.objects.filter(
            posttags__tag__id=self.kwargs['tag_id'])

        return context


class PostPage(HomePage):

    template_name = 'blog_post.html'

    def get_context_data(self, **kwargs):
        context = super(HomePage, self).get_context_data(**kwargs)
        context['post'] = Post.objects.get(id=self.kwargs['post_id'])
        return context
