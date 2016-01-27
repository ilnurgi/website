# coding: utf-8

from django.contrib import admin
from django.db import models


class Category(models.Model):
    name = models.CharField(u'Category name', max_length=50)


class Post(models.Model):

    category = models.ForeignKey(Category)

    title = models.CharField(u'Post title', max_length=100)
    raw_content = models.TextField(u'Post raw content')
    content = models.TextField(u'Post content')

    created = models.DateField(u'Post created date', auto_now_add=True)
    modified = models.DateField(u'Post modified date', auto_now=True)

admin.site.register(Category)
admin.site.register(Post)
