# coding: utf-8
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import Http404
from django.http.response import HttpResponseForbidden
from django.shortcuts import redirect
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from application.views import ConspectsMixin
from blog.models import Post, Category, Comment
from blog.tasks import send_email_notification


class BlogViewMixin(ConspectsMixin):

    def get_context_data(self, **kwargs):
        context = super(BlogViewMixin, self).get_context_data(**kwargs)
        context['active_page'] = 'blog'
        context['categories'] = Category.objects.all()
        return context


class PostListView(BlogViewMixin, ListView):
    model = Post
    paginate_by = 10
    current_category = None

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)

        context['current_category'] = self.current_category
        return context

    def get_queryset(self):
        queryset = super(PostListView, self).get_queryset()

        current_category_name = self.kwargs.get("category_name", "")
        if current_category_name:
            try:
                self.current_category = Category.objects.get(
                    name=current_category_name)
            except Category.DoesNotExist:
                raise Http404()
            else:
                queryset = queryset.filter(category=self.current_category)

        if not self.request.user.is_superuser:
            queryset = queryset.filter(published=True)

        return queryset


class PostDetailView(BlogViewMixin, DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)

        object_comments = self.object.comment_set.all()

        if not self.request.user.is_superuser:
            object_comments = object_comments.filter(published=True)

        context['object_comments'] = object_comments
        return context

    def get_object(self, queryset=None):
        object = super(PostDetailView, self).get_object(queryset=queryset)
        if (object and
                not object.published and
                not self.request.user.is_superuser):
            raise PermissionDenied()
        return object


class PostCreateView(BlogViewMixin, CreateView):
    model = Post
    fields = [
        "title",
        "raw_content",
        "category",
        "published",
    ]

    def get(self, request, *args, **kwargs):
        if not self.request.user.is_superuser:
            raise PermissionDenied()
        return super(PostCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if not self.request.user.is_superuser:
            raise PermissionDenied()
        return super(PostCreateView, self).post(request, *args, **kwargs)


class PostUpdateView(BlogViewMixin, UpdateView):
    model = Post
    fields = [
        "title",
        "raw_content",
        "category",
        "published",
    ]

    def get(self, request, *args, **kwargs):
        if not self.request.user.is_superuser:
            raise PermissionDenied()
        return super(PostUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if not self.request.user.is_superuser:
            raise PermissionDenied()
        return super(PostUpdateView, self).post(request, *args, **kwargs)


class PostDeleteView(BlogViewMixin, DeleteView):
    model = Post
    success_url = reverse_lazy("blog:list", args=[""])

    def get(self, request, *args, **kwargs):
        if not self.request.user.is_superuser:
            raise PermissionDenied()
        return super(PostDeleteView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if not self.request.user.is_superuser:
            raise PermissionDenied()
        return super(PostDeleteView, self).post(request, *args, **kwargs)


def comment_create(request, post_slug):

    if "content_raw" not in request.POST:
        return redirect(reverse("blog:post_detail", args=[post_slug]))

    try:
        post = Post.objects.get(slug=post_slug)
    except Post.DoesNotExist:
        raise Http404()

    if not post.published and not request.user.is_superuser:
        raise PermissionDenied()

    comment = Comment()
    if request.user.is_authenticated():
        comment.user = request.user
    else:
        if ('user_name' not in request.POST or
                'user_email' not in request.POST):
            return redirect(reverse("blog:post_detail", args=[post_slug]))

        comment.user_name = request.POST['user_name']
        comment.user_email = request.POST['user_email']

    comment.content_raw = request.POST['content_raw']
    comment.post = post
    comment.save()

    send_email_notification.delay(
        url=reverse('blog:post_detail', args=[post_slug]))
    return redirect(reverse("blog:post_detail", args=[post_slug]))
