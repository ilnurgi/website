# coding: utf-8

from django.shortcuts import redirect

from application.decorators import (
    superuser_required, superuser_required_in_view)
from application.views import BaseHeaderView
from blog.models import Post, Tags, PostTags


class EditPostPage(BaseHeaderView):

    template_name = 'blog_post_edit.html'

    def get_context_data(self, **kwargs):
        context = super(EditPostPage, self).get_context_data(**kwargs)
        context['active_sub_page'] = 'posts'
        context['tags'] = Tags.objects.all()

        post_id = self.kwargs['post_id']
        if post_id != u'0' and post_id.isdigit():
            context['post'] = Post.objects.get(id=int(post_id))
        return context

    @superuser_required_in_view
    def post(self, request, post_id):
        if post_id != u'0':
            post = Post.objects.get(id=post_id)
        else:
            post = Post()
        post.title = request.POST['post_title']
        post.raw_content = request.POST['post_raw_content']
        post.published = request.POST.get('publish', 'off') == 'on'
        post.save()
        self.create_tags_relation(post, request.POST['tag_names'])
        return redirect('blog:posts_edit', post_id=post.id)

    @staticmethod
    def create_tags_relation(post, tags):
        PostTags.objects.filter(post=post).delete()
        for tag in tags.split(','):
            tag, created = Tags.objects.get_or_create(name=tag.strip().upper())
            PostTags.objects.create(post=post, tag=tag)


@superuser_required
def delete_post(request, post_id):
    Post.objects.filter(id=post_id).delete()
    return redirect('blog:home_page')
