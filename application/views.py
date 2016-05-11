# coding: utf-8

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.template.context_processors import csrf
from django.views.generic import TemplateView, View

from blog.models import Post, PostTags


class IsSuperUserMixin(object):

    def get_context_data(self, **kwargs):
        context = super(IsSuperUserMixin, self).get_context_data(**kwargs)
        context['is_superuser'] = self.request.user.is_superuser
        return context


class CSRFMixin(object):

    def get_context_data(self, **kwargs):
        context = super(CSRFMixin, self).get_context_data(**kwargs)
        context.update(csrf(self.request))
        return context


class HomePage(IsSuperUserMixin, TemplateView):
    template_name = 'index.html'


class SiteMap(IsSuperUserMixin, TemplateView):
    template_name = 'sitemap.html'

    def get_context_data(self, **kwargs):
        context = super(SiteMap, self).get_context_data(**kwargs)

        post_tags = PostTags.objects
        if not self.request.user.is_superuser:
            post_tags = post_tags.filter(post__published=True)

        post_tags = post_tags.select_related()
        group_posts = {}
        for post_tag in post_tags:
            group_posts.setdefault(post_tag.tag, []).append(post_tag.post)

        for value in group_posts.values():
            value.sort(key=lambda x: x.title)

        group_posts = group_posts.items()
        group_posts.sort(key=lambda x: x[0].name)

        context['active_page'] = 'sitemap'
        context['group_posts'] = group_posts
        return context


class Login(IsSuperUserMixin, CSRFMixin, TemplateView):
    template_name = 'login.html'

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
