# coding: utf-8

import datetime
import json

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
        context['active_page_sub'] = 'system'
        return context


class Visiters(HomePage):

    template_name = 'metrics_visiters.html'

    def get_context_data(self, **kwargs):
        context = super(Visiters, self).get_context_data(**kwargs)
        context['active_page_sub'] = 'visiters'
        return context


class URLS(HomePage):

    template_name = 'metrics_urls.html'

    def get_context_data(self, **kwargs):
        context = super(URLS, self).get_context_data(**kwargs)
        context['active_page_sub'] = 'urls'

        mongo_client = pymongo.MongoClient(
            settings.DATABASE_MONGO['host'],
            int(settings.DATABASE_MONGO['port']))

        db = mongo_client[settings.DATABASE_MONGO['nginx_access_db_name']]

        docs = db.month_report.find().sort('date', -1)
        context['urls'] = []

        for doc in docs:
            urls = json.loads(doc['urls']).items()
            urls.sort(key=lambda x: x[1], reverse=True)
            context['urls'].append({
                'date': doc['date'],
                'urls': urls
            })

        return context


class URLSFrom(HomePage):

    template_name = 'metrics_urls.html'

    def get_context_data(self, **kwargs):
        context = super(URLSFrom, self).get_context_data(**kwargs)
        context['active_page_sub'] = 'urls_from'

        mongo_client = pymongo.MongoClient(
            settings.DATABASE_MONGO['host'],
            int(settings.DATABASE_MONGO['port']))

        db = mongo_client[settings.DATABASE_MONGO['nginx_access_db_name']]

        docs = db.month_report.find().sort('date', -1)
        context['urls'] = []

        for doc in docs:
            urls = json.loads(doc['urls_from']).items()
            urls.sort(key=lambda x: x[1], reverse=True)
            context['urls'].append({
                'date': doc['date'],
                'urls': urls
            })

        return context


class UserAgents(HomePage):

    template_name = 'metrics_urls.html'

    def get_context_data(self, **kwargs):
        context = super(UserAgents, self).get_context_data(**kwargs)
        context['active_page_sub'] = 'user_agents'

        mongo_client = pymongo.MongoClient(
            settings.DATABASE_MONGO['host'],
            int(settings.DATABASE_MONGO['port']))

        db = mongo_client[settings.DATABASE_MONGO['nginx_access_db_name']]

        docs = db.month_report.find().sort('date', -1)
        context['urls'] = []

        for doc in docs:
            urls = json.loads(doc['user_agents']).items()
            urls.sort(key=lambda x: x[1], reverse=True)
            context['urls'].append({
                'date': doc['date'],
                'urls': urls
            })

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


def ip_data(requset):
    mongo_client = pymongo.MongoClient(
        settings.DATABASE_MONGO['host'],
        int(settings.DATABASE_MONGO['port']))

    db = mongo_client[settings.DATABASE_MONGO['nginx_access_db_name']]

    times = []
    times_append = times.append

    _ip_data = []
    ip_data_append = _ip_data.append

    _ip_uniq_data = []
    ip_uniq_data_append = _ip_uniq_data.append

    for i in db.month_report.find().sort('date'):
        times_append(i['date'].strftime('%d.%m.%Y'))
        ip_data_append(i['ip_count'])
        ip_uniq_data_append(i['ip_uniq_count'])

    return JsonResponse({
        'labels': times,
        'ip_data': _ip_data,
        'ip_uniq_data': _ip_uniq_data
    })
