# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Tag',
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-created']},
        ),
        migrations.AddField(
            model_name='post',
            name='description',
            field=models.CharField(max_length=255, null=True, verbose_name='Description'),
        ),
    ]
