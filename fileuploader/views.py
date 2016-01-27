# coding: utf-8

from django.shortcuts import redirect
from django.views.generic import TemplateView

from application.views import IsSuperUserMixin, CSRFMixin
from fileuploader.models import File


class HomePage(IsSuperUserMixin, CSRFMixin, TemplateView):

    template_name = 'base_fileuploader.html'

    def get_context_data(self, **kwargs):
        context = super(HomePage, self).get_context_data(**kwargs)
        context['active_page'] = 'fileuploader'
        context['files'] = File.objects.order_by('-id')
        return context

    def post(self, request):
        if 'file' in request.FILES:
            f = request.FILES['file']
            File(file=f, file_name=f.name).save()
        return redirect('fileuploader:home_page')
