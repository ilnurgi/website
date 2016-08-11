# coding: utf-8

from django.contrib.auth import logout, authenticate, login
from django.shortcuts import redirect
from django.views.generic import View, TemplateView

from application.views.mixins import IsSuperUserMixin, CSRFMixin, ConspectsMixin
from blog.models import PostTags


class BaseHeaderView(IsSuperUserMixin, ConspectsMixin, TemplateView):
    """
    базовый класс для страниц с шапкой
    """


class Logout(View):

    def get(self, request):
        logout(request)
        return redirect('home_page')


class Login(CSRFMixin, BaseHeaderView):
    template_name = 'login.html'

    def post(self, request):
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
        return redirect('home_page')


class SiteMap(BaseHeaderView):
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


class HomePage(BaseHeaderView):
    template_name = '_index.html'


class ConspectsPage(BaseHeaderView):
    template_name = 'conspects.html'
