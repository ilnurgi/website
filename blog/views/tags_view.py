# coding: utf-8

from django.shortcuts import redirect

from application.decorators import (
    superuser_required, superuser_required_in_view)
from application.views import BaseHeaderView
from blog.models import Tags, PostTags


class TagsPage(BaseHeaderView):

    template_name = 'blog_tags.html'

    def get_context_data(self, **kwargs):
        context = super(TagsPage, self).get_context_data(**kwargs)
        context['tags'] = Tags.objects.all()
        context['active_sub_page'] = 'tags'
        return context

    @superuser_required_in_view
    def post(self, request):
        tag_name = request.POST['name'].upper()
        if not Tags.objects.filter(name=tag_name).exists():
            Tags.objects.create(name=tag_name)
        return redirect('blog:tags')


class TagsEditPage(TagsPage):

    def get_context_data(self, **kwargs):
        context = super(TagsEditPage, self).get_context_data(**kwargs)
        context['tags'] = Tags.objects.all()
        context['tag'] = Tags.objects.get(id=self.kwargs['tag_id'])
        return context

    @superuser_required_in_view
    def post(self, request, tag_id):
        tag_name = request.POST['name'].upper()
        Tags.objects.filter(id=tag_id).update(name=tag_name)
        return redirect('blog:tags')


@superuser_required
def tag_delete(request, tag_id):
    if not PostTags.objects.filter(tag_id=tag_id).exists():
        Tags.objects.filter(id=tag_id).delete()
    return redirect('blog:tags')
