# coding: utf-8

import datetime

import pymongo

from django.conf import settings
from django.http import JsonResponse
from django.views.generic import TemplateView, View


mongo_client = pymongo.MongoClient(
    settings.DATABASE_MONGO['host'],
    int(settings.DATABASE_MONGO['port'])
)


class MetricsHomePage(TemplateView):

    template_name = 'metrics.html'

    def get_context_data(self, **kwargs):
        context = super(MetricsHomePage, self).get_context_data(**kwargs)
        context['active_page'] = 'metrics'
        context['active_page_sub'] = 'visiters'

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








