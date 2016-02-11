# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20160203_0816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Post created date'),
        ),
        migrations.AlterField(
            model_name='post',
            name='modified',
            field=models.DateTimeField(auto_now=True, verbose_name='Post modified date'),
        ),
    ]
