# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostTags',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='Tags name')),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.AddField(
            model_name='posttags',
            name='post',
            field=models.ForeignKey(to='blog.Post'),
        ),
        migrations.AddField(
            model_name='posttags',
            name='tag',
            field=models.ForeignKey(to='blog.Tags'),
        ),
    ]
