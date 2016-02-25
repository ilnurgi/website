# coding: utf-8

from django.contrib import admin
from django.contrib.auth.models import User
from django.db import models


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

    def __unicode__(self):
        return u'{0}'.format(
            self.user or u'{0} / {1}'.format(self.user_name, self.user_email))

admin.site.register(Comment)
