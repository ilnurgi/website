# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_name', models.CharField(max_length=50, null=True, verbose_name='Anonim username')),
                ('user_email', models.CharField(max_length=50, null=True, verbose_name='Anonim email')),
                ('content', models.TextField()),
                ('content_raw', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Comment created date')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Comment modified date')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
    ]
