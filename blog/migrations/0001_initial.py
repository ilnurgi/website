# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='Category name')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name='Post title')),
                ('raw_content', models.TextField(verbose_name='Post raw content')),
                ('content', models.TextField(verbose_name='Post content')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Post created date')),
                ('modified', models.DateField(auto_now=True, verbose_name='Post modified date')),
                ('category', models.ForeignKey(to='blog.Category')),
            ],
        ),
    ]
