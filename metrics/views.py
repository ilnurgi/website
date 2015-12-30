# coding: utf-8

import datetime

import pymongo

from django.conf import settings
from django.http import JsonResponse
from django.views.generic import TemplateView, View
from pymongo.mongo_client import MongoClient

mongo_client = pymongo.MongoClient(
    settings.DATABASE_MONGO['host'],
    int(settings.DATABASE_MONGO['port'])
)


class MetricsHomePage(TemplateView):

    template_name = 'base_metrics.html'


class MetricsCpu(TemplateView):

    template_name = 'metrics_cpu.html'

    def get_context_data(self, **kwargs):
        context = super(MetricsCpu, self).get_context_data(**kwargs)

        mongo_client = MongoClient(
            settings.DATABASE_MONGO['host'],
            int(settings.DATABASE_MONGO['port']))

        db = mongo_client[settings.DATABASE_MONGO['cpu_average_db_name']]
        # collection_average_hour = db.average_hour

        cpu_minute_times = []
        cpu_minute_times_append = cpu_minute_times.append

        cpu_minute_average = []
        cpu_minute_average_append = cpu_minute_average.append

        for i in db.average_minute.find():
            cpu_minute_times_append(i['date'].strftime('%H:%M'))
            cpu_minute_average_append(i['percent'])

        # context['cpu_minute_times'] = u','.join(cpu_minute_times)
        context['cpu_minute_times'] = cpu_minute_times
        # context['cpu_minute_average'] = u','.join(cpu_minute_average)
        context['cpu_minute_average'] = cpu_minute_average
        context['active_page'] = 'metrics'
        context['active_page_sub'] = 'cpu'
        return context


class LastMonthVisiters(View):
    """
    возвращаем данные для Chart.js вида
     {
        'days': [...],
        'value': [...]
     }
    """

    def get(self, request):
        return JsonResponse({'1':'123'})

        # data = {
        #     'uniq_ips': {
        #         'days': [],
        #         'counts': []
        #     }
        # }
        #
        # date = None
        # uniq_ips = set()
        #
        # for log in mongo_db.log.find().sort('date', pymongo.ASCENDING):
        #     date =








