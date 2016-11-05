# coding: utf-8

from django.contrib import admin

from . import models

admin.site.register(models.CarColor)
admin.site.register(models.Car)
admin.site.register(models.CarModel)
admin.site.register(models.CarPhoto)
