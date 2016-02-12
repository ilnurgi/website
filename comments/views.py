# coding: utf-8

from django.shortcuts import redirect
from django.views.generic import TemplateView

from markdown import markdown

from application.decorators import (
    superuser_required_in_view, superuser_required)
from application.views import IsSuperUserMixin

from comments.models import Comment


class HomePage(IsSuperUserMixin, TemplateView):

    template_name = 'base_comments.html'

    @superuser_required_in_view
    def get(self, request, *args, **kwargs):
        return super(HomePage, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(HomePage, self).get_context_data(**kwargs)
        context['comments'] = Comment.objects.all()
        return context


class EditPage(IsSuperUserMixin, TemplateView):

    template_name = 'comments_edit.html'

    @superuser_required_in_view
    def get(self, request, *args, **kwargs):
        return super(EditPage, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(EditPage, self).get_context_data(**kwargs)
        context['comment'] = Comment.objects.get(id=self.kwargs['comment_id'])
        context['redirect'] = self.request.GET.get('redirect', None)
        return context

    @superuser_required_in_view
    def post(self, request, comment_id):
        comment = Comment.objects.get(id=comment_id)
        comment.user_name = request.POST['user_name']
        comment.user_email = request.POST['user_email']
        comment.content = markdown(request.POST['content_raw'])
        comment.content_raw = request.POST['content_raw']
        comment.save()
        if request.POST['redirect']:
            return redirect(request.POST['redirect'])
        return redirect('comments:edit', comment_id=comment_id)


@superuser_required
def comment_delete(request, comment_id):
    Comment.objects.filter(id=comment_id).delete()
    if 'redirect' in request.GET:
        return redirect(request.GET['redirect'])
    return redirect('comments:home_page')
