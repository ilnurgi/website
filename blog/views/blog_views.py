# coding: utf-8

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.views.generic import TemplateView

from markdown import markdown

from application.views import IsSuperUserMixin, CSRFMixin
from blog.models import Tags, Post, PostComments
from blog.tasks import send_email_notification
from comments.models import Comment


POSTS_IN_PAGE = 10


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

        posts = self.get_posts()
        page = self.request.GET.get('page')
        paginator = Paginator(posts, POSTS_IN_PAGE)
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)

        context['posts'] = posts
        return context

    def get_posts(self):
        posts = Post.objects.all()
        if not self.request.user.is_superuser:
            posts = posts.filter(published=True)
        return posts


class TagPage(HomePage):

    def get_context_data(self, **kwargs):
        context = super(TagPage, self).get_context_data(**kwargs)
        context['current_tag_id'] = self.kwargs['tag_id']
        return context

    def get_posts(self):
        posts = super(TagPage, self).get_posts()
        return posts.filter(
            posttags__tag__id=self.kwargs['tag_id'])


class PostPage(CSRFMixin, HomePage):

    template_name = 'blog_post.html'

    def get_context_data(self, **kwargs):
        context = super(HomePage, self).get_context_data(**kwargs)
        context['post'] = Post.objects.get(id=self.kwargs['post_id'])
        comments = Comment.objects.filter(
            postcomments__post=context['post'])

        if not self.request.user.is_superuser:
            comments = comments.filter(published=True)

        context['post_comments'] = comments.order_by('-created')
        context['user'] = self.request.user
        return context


def comment_add(request, post_id):
    comment = Comment()
    if request.user.is_authenticated():
        comment.user = request.user
    else:
        if ('user_name' not in request.POST or
                'user_email' not in request.POST):
            return redirect(request.GET.get('redirect', '/'))

        comment.user_name = request.POST['user_name']
        comment.user_email = request.POST['user_email']
    comment.content = markdown(request.POST['content_raw'])
    comment.content_raw = request.POST['content_raw']
    comment.save()

    PostComments.objects.create(post_id=post_id, comment_id=comment.id)
    send_email_notification.delay(
        url=reverse('blog:post_page', kwargs={'post_id': post_id}))
    return redirect(request.GET.get('redirect', '/'))
