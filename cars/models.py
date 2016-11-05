# coding: utf-8

import os

from django.db import models


def upload_car_model_image(instance, file_name):
    return os.path.join(
        u"cars", instance.name, u"title.png")


def upload_car_image(instance, file_name):
    return os.path.join(
        u"cars", instance.model.name, instance.name, u"title.png")


def upload_photo_image(instance, file_name):
    return os.path.join(
        u"cars",
        instance.car.model.name,
        instance.car.name,
        instance.color.name,
        file_name)


class CarModel(models.Model):
    """
    марка автомобиля
    """
    name = models.CharField(max_length=100)
    image = models.FileField(upload_to=upload_car_model_image)

    def __unicode__(self):
        return unicode(self.name)


class CarColor(models.Model):
    """
    цвет
    """
    name = models.CharField(max_length=100)
    hex = models.CharField(max_length=7)

    def __unicode__(self):
        return u'{0}: {1}'.format(self.name, self.hex)


class Car(models.Model):
    """
    автомобиль
    """
    model = models.ForeignKey(CarModel)
    name = models.CharField(max_length=100)
    image = models.FileField(upload_to=upload_car_image)

    def __unicode__(self):
        return u'{0} {1}'.format(self.model, self.name)


class CarPhoto(models.Model):
    """
    фотография машины
    """
    car = models.ForeignKey(Car)
    image = models.FileField(upload_to=upload_photo_image)
    color = models.ForeignKey(CarColor)

    def __unicode__(self):
        return u'{0} {1}'.format(self.car, self.color)
