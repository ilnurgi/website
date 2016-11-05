# coding: utf-8

import re
from StringIO import StringIO

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models

from markdown import markdown

from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter

from pytils.translit import slugify

import lxml.html as html


class Category(models.Model):

    name = models.CharField(u'Name', max_length=50, unique=True)

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name


class Post(models.Model):

    title = models.CharField(u'Post title', max_length=100)
    raw_content = models.TextField(u'Post raw content')
    content = models.TextField(u'Post content')
    published = models.BooleanField(default=False)
    category = models.ForeignKey(Category)

    created = models.DateTimeField(u'Post created date', auto_now_add=True)
    modified = models.DateTimeField(u'Post modified date', auto_now=True)

    slug = models.SlugField(blank=True, unique=True)

    description = models.CharField(u'Description', max_length=255)

    re_references = re.compile(ur'\[(.+?)\]\[(.+?)\]')
    re_files = re.compile(ur'(\[FILE=(\d+)\])')

    class Meta:
        ordering = ['-created']

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:post_detail", args=[self.category.name, self.slug])

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.content = (
            self.set_tables_classes(
                self.add_files(
                    self.add_code_style(
                        markdown(
                            self.add_url_references(
                                self.raw_content),
                            extensions=['tables']
                        )))))
        self.slug = slugify(self.title)

        super(Post, self).save(
            force_insert=force_insert,
            force_update=force_update,
            using=using,
            update_fields=update_fields)

    def add_files(self, content):
        finds = self.re_files.findall(content)
        file_ids = [int(file_id) for _, file_id in finds]
        file_ids_map = {
            f.id: f for f in File.objects.filter(id__in=file_ids)
        }
        for replacer, file_id in finds:
            f = file_ids_map.get(int(file_id))
            if f:
                content = content.replace(
                    replacer,
                    f.file.url)

        return content

    def add_url_references(self, content):
        """
        добавляем урлы ссылок для документации
        """
        refs = set([ref for title, ref in self.re_references.findall(content)])
        refs = {
            ref.socr: ref.url
            for ref in DocsReferenc.objects.filter(socr__in=refs)
        }

        for title, ref in set(self.re_references.findall(content)):
            if ref in refs:
                content = content.replace(
                    u'[{0}][{1}]'.format(title, ref),
                    u'[{0}]({1})'.format(title, refs[ref]))

        return content

    def add_code_style(self, content):
        """
        добавялем подсветку кода
        """
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
                try:
                    lexer = get_lexer_by_name(_lexer, stripall=True)
                except ValueError:
                    lexer = get_lexer_by_name('text', stripall=True)
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

    def set_tables_classes(self, content):
        """
        добавляет классы для таблиц
        :param content:
        :return:
        """
        root = html.parse(StringIO(content))
        table_wrappers = root.xpath('//div[@class="table_wrapper"]')
        for table_wrapper in table_wrappers:
            table = table_wrapper.getnext()
            if table:
                table.attrib['class'] = table_wrapper.attrib.get(
                    'data-table-class', "")
        return html.tostring(root)

    def tag_names(self):
        return u', '.join(
            unicode(pt.tag) for pt in self.posttags_set.order_by('tag__name'))


class DocsReferenc(models.Model):

    category = models.ForeignKey(Category)
    socr = models.CharField(max_length=100, unique=True)
    url = models.URLField(unique=True)

    def __unicode__(self):
        return u'{0} / {1}'.format(self.socr, self.url)


class Comment(models.Model):

    user = models.ForeignKey(User, null=True, blank=True)
    user_name = models.CharField(
        u'Anonim username', max_length=50, null=True, blank=True)
    user_email = models.CharField(
        u'Anonim email', max_length=50, null=True, blank=True)

    content = models.TextField()
    content_raw = models.TextField()

    published = models.BooleanField(default=False)

    created = models.DateTimeField(u'Comment created date', auto_now_add=True)
    modified = models.DateTimeField(u'Comment modified date', auto_now=True)

    post = models.ForeignKey(Post)

    class Meta:
        ordering = ['-created']

    def __unicode__(self):
        return u'{0}'.format(
            self.user or u'{0} / {1}'.format(self.user_name, self.user_email))

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.content = markdown(self.content_raw)
        super(Comment, self).save(
            force_insert=force_insert,
            force_update=force_update,
            using=using,
            update_fields=update_fields)


class File(models.Model):
    file_name = models.CharField(max_length=100, blank=True)
    file = models.FileField()
    created = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return unicode(self.file)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.file_name = self.file.name
        super(File, self).save(
            force_insert=force_insert,
            force_update=force_update,
            using=using,
            update_fields=update_fields)
