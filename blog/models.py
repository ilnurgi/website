# coding: utf-8

import re

from django.contrib import admin
from django.db import models
from markdown import markdown

from comments.models import Comment

re_references = re.compile(ur'\[(.+?)\]\[(.+?)\]')
re_pre_code = re.compile(ur'<pre><code>(.+?)</code></pre>')
re_unicode = re.compile(ur'(u\'(.*?)\')')


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
