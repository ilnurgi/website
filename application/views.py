# coding: utf-8

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.template.context_processors import csrf
from django.views.generic import TemplateView, View


class IsSuperUserMixin(object):

    def get_context_data(self, **kwargs):
        context = super(IsSuperUserMixin, self).get_context_data(**kwargs)
        context['is_superuser'] = self.request.user.is_superuser
        return context


class HomePage(IsSuperUserMixin, TemplateView):
    template_name = 'index.html'


class Login(IsSuperUserMixin, TemplateView):
    template_name = 'login.html'

    def get_context_data(self, **kwargs):
        context = super(Login, self).get_context_data(**kwargs)
        context.update(csrf(self.request))
        return context

    def post(self, request):
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
        return redirect('home_page')


class Logout(View):

    def get(self, request):
        logout(request)
        return redirect('home_page')
