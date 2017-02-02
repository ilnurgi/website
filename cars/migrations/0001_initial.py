# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import cars.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('image', models.FileField(upload_to=cars.models.upload_car_image)),
            ],
        ),
        migrations.CreateModel(
            name='CarColor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('hex', models.CharField(max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('image', models.FileField(upload_to=cars.models.upload_car_model_image)),
            ],
        ),
        migrations.CreateModel(
            name='CarPhoto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.FileField(upload_to=cars.models.upload_photo_image)),
                ('car', models.ForeignKey(to='cars.Car')),
                ('color', models.ForeignKey(to='cars.CarColor')),
            ],
        ),
        migrations.AddField(
            model_name='car',
            name='model',
            field=models.ForeignKey(to='cars.CarModel'),
        ),
    ]
