# coding: utf-8

from django.http.response import JsonResponse
from django.shortcuts import render_to_response

from .models import CarPhoto


def index(request):
    return render_to_response("cars.html")


def data(request):
    result = []

    for car_photo in CarPhoto.objects.select_related():
        try:
            car_model = [
                car_model for car_model in result
                if car_model["name"] == car_photo.car.model.name][0]
        except IndexError:
            car_model = {
                "name": car_photo.car.model.name,
                "image_url": car_photo.car.model.image.url,
                "cars": []
            }
            result.append(car_model)

        try:
            car = [
                car for car in car_model["cars"]
                if car["name"] == car_photo.car.name][0]
        except IndexError:
            car = {
                "name": car_photo.car.name,
                "image_url": car_photo.car.image.url,
                "colors": []
            }
            car_model["cars"].append(car)

        try:
            color = [
                color for color in car["colors"]
                if color["name"] == car_photo.color.name][0]
        except IndexError:
            color = {
                "name": car_photo.color.name,
                "hex": car_photo.color.hex,
                "images": []
            }
            car["colors"].append(color)

        color["images"].append(car_photo.image.url)
    return JsonResponse(result, safe=False)
