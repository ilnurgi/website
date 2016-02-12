# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
        ('blog', '0003_auto_20160203_0849'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostComments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment', models.ForeignKey(to='comments.Comment')),
            ],
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created']},
        ),
        migrations.AlterModelOptions(
            name='tags',
            options={'ordering': ['name']},
        ),
        migrations.AddField(
            model_name='postcomments',
            name='post',
            field=models.ForeignKey(to='blog.Post'),
        ),
    ]
