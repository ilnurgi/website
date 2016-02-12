# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='published',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='user_email',
            field=models.CharField(max_length=50, null=True, verbose_name='Anonim email', blank=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='user_name',
            field=models.CharField(max_length=50, null=True, verbose_name='Anonim username', blank=True),
        ),
    ]
