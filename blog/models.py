# coding: utf-8

from django.contrib import admin
from django.db import models

from comments.models import Comment


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
