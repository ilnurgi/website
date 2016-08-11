# coding: utf-8

import os

from django.shortcuts import redirect

from application.views.mixins import CSRFMixin
from application.views import BaseHeaderView
from fileuploader.models import File


class HomePage(CSRFMixin, BaseHeaderView):

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


def delete(request, file_id):
    fl = File.objects.get(id=file_id)
    if os.path.exists(fl.file.path):
        os.remove(fl.file.path)
    fl.delete()

    return redirect('fileuploader:home_page')
