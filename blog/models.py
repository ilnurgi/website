# coding: utf-8

import re

from django.contrib import admin
from django.db import models

from markdown import markdown

from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter

from comments.models import Comment

re_references = re.compile(ur'\[(.+?)\]\[(.+?)\]')


class Tags(models.Model):

    name = models.CharField(u'Tags name', max_length=50)

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name


class Post(models.Model):

    title = models.CharField(u'Post title', max_length=100)
    raw_content = models.TextField(u'Post raw content')
    content = models.TextField(u'Post content')
    published = models.BooleanField(default=False)

    created = models.DateTimeField(u'Post created date', auto_now_add=True)
    modified = models.DateTimeField(u'Post modified date', auto_now=True)

    class Meta:
        ordering = ['-created']

    def __unicode__(self):
        return self.title

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.content = self.add_code_style(
            markdown(
                self.add_url_references(self.raw_content)))
        super(Post, self).save(
            force_insert=force_insert, force_update=force_update, using=using,
            update_fields=update_fields)

    def add_url_references(self, content):
        refs = set([ref for title, ref in re_references.findall(content)])
        refs = {
            ref.socr: ref.url
            for ref in DocsReferences.objects.filter(socr__in=refs)
        }

        for title, ref in set(re_references.findall(content)):
            if ref in refs:
                content = content.replace(
                    u'[{0}][{1}]'.format(title, ref),
                    u'[{0}]({1})'.format(title, refs[ref]))

        return content

    def add_code_style(self, content):
        code_start = u'<pre><code>'
        code_end = u'</code></pre>'
        code_start_len = len(code_start)

        is_code = False
        _lexer = 'text'
        code = []
        result = []

        for line in content.splitlines():
            if line.startswith(code_start):
                is_code = True
                _lexer = line[code_start_len:].strip()
            elif line.endswith(code_end):
                is_code = False
                lexer = get_lexer_by_name(_lexer, stripall=True)
                formatter = HtmlFormatter()
                result.append(
                    highlight(
                        u'\n'.join(
                            i.replace('&lt;', '<').replace('&gt;', '>')
                            for i in code),
                        lexer,
                        formatter))
                code = []
            elif is_code:
                code.append(line)
            else:
                result.append(line)

        return u'\n'.join(result)

    def tag_names(self):
        return u', '.join(
            unicode(pt.tag) for pt in self.posttags_set.order_by('tag__name'))


class PostTags(models.Model):

    post = models.ForeignKey(Post)
    tag = models.ForeignKey(Tags)

    def __unicode__(self):
        return u'{0}/{1}'.format(self.tag, self.post)


class PostComments(models.Model):

    post = models.ForeignKey(Post)
    comment = models.ForeignKey(Comment)


class DocsReferences(models.Model):

    socr = models.CharField(max_length=100, unique=True)
    url = models.URLField(unique=True)

    def __unicode__(self):
        return u'{0} / {1}'.format(self.socr, self.url)

admin.site.register(Tags)
admin.site.register(Post)
admin.site.register(PostTags)
admin.site.register(PostComments)
admin.site.register(DocsReferences)
