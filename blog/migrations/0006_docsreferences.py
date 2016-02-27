# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post_published'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocsReferences',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('socr', models.CharField(unique=True, max_length=100)),
                ('url', models.URLField(unique=True)),
            ],
        ),
    ]
