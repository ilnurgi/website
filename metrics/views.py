# coding: utf-8

import datetime

import pymongo

from django.conf import settings
from django.http import JsonResponse
from django.views.generic import TemplateView

from application.views import IsSuperUserMixin


class HomePage(IsSuperUserMixin, TemplateView):

    template_name = 'base_metrics.html'

    def get_context_data(self, **kwargs):
        context = super(HomePage, self).get_context_data(**kwargs)
        context['active_page'] = 'metrics'
        return context


class System(HomePage):

    template_name = 'metrics_system.html'

    def get_context_data(self, **kwargs):
        context = super(System, self).get_context_data(**kwargs)
        context['active_page_sub'] = 'cpu'
        return context


def cpu_data(request):
    mongo_client = pymongo.MongoClient(
        settings.DATABASE_MONGO['host'],
        int(settings.DATABASE_MONGO['port']))

    db = mongo_client[settings.DATABASE_MONGO['cpu_average_db_name']]

    cpu_times = []
    cpu_times_append = cpu_times.append

    cpu_average = []
    cpu_average_append = cpu_average.append

    for i in db.average_minute.find({
        'date': {
            '$gte': datetime.datetime.now() - datetime.timedelta(minutes=30)
        }
    }).sort('date'):
        cpu_times_append(i['date'].strftime('%H:%M'))
        cpu_average_append(i['percent'])
    return JsonResponse({
        'labels': cpu_times,
        'data': cpu_average
    })


def cpu_hour_data(request):
    mongo_client = pymongo.MongoClient(
        settings.DATABASE_MONGO['host'],
        int(settings.DATABASE_MONGO['port']))

    db = mongo_client[settings.DATABASE_MONGO['cpu_average_db_name']]

    cpu_times = []
    cpu_times_append = cpu_times.append

    cpu_average = []
    cpu_average_append = cpu_average.append

    for i in db.average_hour.find().sort('date'):
        cpu_times_append(i['date'].strftime('%d.%m.%Y (%H)'))
        cpu_average_append(i['percent'])
    return JsonResponse({
        'labels': cpu_times,
        'data': cpu_average
    })


def mem_data(request):
    mongo_client = pymongo.MongoClient(
        settings.DATABASE_MONGO['host'],
        int(settings.DATABASE_MONGO['port']))

    db = mongo_client[settings.DATABASE_MONGO['mem_average_db_name']]

    cpu_times = []
    cpu_times_append = cpu_times.append

    cpu_average = []
    cpu_average_append = cpu_average.append

    for i in db.average_minute.find({
        'date': {
            '$gte': datetime.datetime.now() - datetime.timedelta(minutes=30)
        }
    }).sort('date'):
        cpu_times_append(i['date'].strftime('%H:%M'))
        cpu_average_append(i['percent'])
    return JsonResponse({
        'labels': cpu_times,
        'data': cpu_average
    })


def mem_hour_data(request):
    mongo_client = pymongo.MongoClient(
        settings.DATABASE_MONGO['host'],
        int(settings.DATABASE_MONGO['port']))

    db = mongo_client[settings.DATABASE_MONGO['mem_average_db_name']]

    cpu_times = []
    cpu_times_append = cpu_times.append

    cpu_average = []
    cpu_average_append = cpu_average.append

    for i in db.average_hour.find().sort('date'):
        cpu_times_append(i['date'].strftime('%d.%m.%Y (%H)'))
        cpu_average_append(i['percent'])
    return JsonResponse({
        'labels': cpu_times,
        'data': cpu_average
    })
