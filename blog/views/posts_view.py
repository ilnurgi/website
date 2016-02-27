# coding: utf-8

import re

from markdown import markdown

from django.shortcuts import redirect
from django.views.generic import TemplateView

from application.decorators import (
    superuser_required, superuser_required_in_view)
from application.views import IsSuperUserMixin
from blog.models import Post, Tags, PostTags, DocsReferences


re_references = re.compile(ur'\[(.+?)\]\[(.+?)\]')
re_pre_code = re.compile(ur'<pre><code>(.+?)</code></pre>')
re_unicode = re.compile(ur'(u\'(.*?)\')')


class EditPostPage(IsSuperUserMixin, TemplateView):

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
        post.content = self.add_code_style(
            markdown(
                self.add_url_references(
                    request.POST['post_raw_content'])))
        post.published = request.POST.get('publish', 'off') == 'on'
        post.save()
        self.create_tags_relation(post, request.POST['tag_names'])
        return redirect('blog:posts_edit', post_id=post.id)

    def add_url_references(self, content):
        titles = set([title for title, ref in re_references.findall(content)])
        refs = {
            ref.socr: ref.url
            for ref in DocsReferences.objects.filter(socr__in=titles)
        }
        for title, ref in set(re_references.findall(content)):
            if title in refs:
                content = content.replace(
                    u'[{0}][{1}]'.format(title, ref),
                    u'[{0}]({1})'.format(title, refs[title]))

        return content

    def add_code_style(self, content):
        print 'add_code_style'
        is_code = False
        code_start = u'<pre><code>'
        code_end = u'</code></pre>'
        code_start_len = len(code_start)
        code_end_len = len(code_end)
        _content = []

        for line in content.split('\n'):
            if line.startswith(code_start):
                is_code = True
                _line = line[code_start_len:]
            elif line.endswith(code_end):
                is_code = False
                _line = line[:code_end_len]
            else:
                _line = line

            _new_line = _line
            if is_code:
                if _new_line.strip().startswith(u'#'):
                    _new_line = u'<span class="comment">{0}</span>'.format(
                        _new_line)
                else:
                    for kw in (u'import ', u'try:', u'except ', u'print ',
                               u'if ', u'is not ', u'not ', u'for ', u'in '):
                        if _new_line.startswith(kw):
                            _new_line = _new_line.replace(
                                kw.strip(),
                                u'<span class="keyword">{0}</span>'.format(
                                    kw.strip()),
                                1)
                        else:
                            _new_line = _new_line.replace(
                                u' {0}'.format(kw),
                                u' <span class="keyword">{0}</span> '.format(
                                    kw.strip()))

                    for kw in (u'True', u'False'):
                        if _new_line.startswith(u'{0} '.format(kw)):
                            _new_line = _new_line.replace(
                                kw,
                                u'<span class="bool">{0}</span>'.format(
                                    kw.strip()),
                                1)
                        else:
                            _new_line = _new_line.replace(
                                u' {0} '.format(kw),
                                u' <span class="bool">{0}</span> '.format(
                                    kw.strip())).replace(
                                u' {0}:'.format(kw),
                                u' <span class="bool">{0}:</span>'.format(
                                    kw.strip()))

                    for exc in (u'IndexError', ):
                        _new_line = _new_line.replace(
                            u' {0}:'.format(exc),
                            u'<span class="exception"> {0}:</span>'.format(exc))

                    for items in re_unicode.findall(_new_line):
                        _new_line = _new_line.replace(
                            items[0],
                            u'<span class="unicode">u</span>'
                            u'<span class="string">\'{0}\'</span>'.format(
                                items[1]))

            _content.append(line.replace(_line, _new_line))

        return u'\n'.join(_content)

    def create_tags_relation(self, post, tags):
        PostTags.objects.filter(post=post).delete()
        for tag in tags.split(','):
            tag, created = Tags.objects.get_or_create(name=tag.strip().upper())
            PostTags.objects.create(post=post, tag=tag)


@superuser_required
def delete_post(request, post_id):
    Post.objects.filter(id=post_id).delete()
    return redirect('blog:home_page')
