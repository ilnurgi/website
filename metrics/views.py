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


def docs_data(request):
    mongo_client = pymongo.MongoClient(
        settings.DATABASE_MONGO['host'],
        int(settings.DATABASE_MONGO['port']))

    db = mongo_client[settings.DATABASE_MONGO['nginx_access_db_name']]

    times = []
    times_append = times.append

    _docs_data = []
    docs_data_append = _docs_data.append

    for i in db.month_report.find().sort('date'):
        times_append(i['date'].strftime('%d.%m.%Y'))
        counter = 0
        for url, count in json.loads(i['urls']).iteritems():
            if url.startswith('/docs/'):
                counter += count
        docs_data_append(counter)

    return JsonResponse({
        'labels': times,
        'data': _docs_data
    })


def docs_data_all(request):
    mongo_client = pymongo.MongoClient(
        settings.DATABASE_MONGO['host'],
        int(settings.DATABASE_MONGO['port']))

    db = mongo_client[settings.DATABASE_MONGO['nginx_access_db_name']]

    times = []
    times_append = times.append

    data = {
        'android': [],
        'java': [],
        'droidscript': [],
        'python': [],
        'p4a': [],
        'pys60': [],
        'html': [],
        'css': [],
        'js': [],
        'jq': [],
        'angular': [],
        'sql': [],
        'linux': [],
    }
    data_android_append = data['android'].append
    data_java_append = data['java'].append
    data_droidscript_append = data['droidscript'].append
    data_python_append = data['python'].append
    data_p4a_append = data['p4a'].append
    data_pys60_append = data['pys60'].append
    data_html_append = data['html'].append
    data_css_append = data['css'].append
    data_js_append = data['js'].append
    data_jq_append = data['jq'].append
    data_angular_append = data['angular'].append
    data_sql_append = data['sql'].append
    data_linux_append = data['linux'].append

    for i in db.month_report.find().sort('date'):
        times_append(i['date'].strftime('%d.%m.%Y'))

        counter_android = 0
        counter_java = 0
        counter_droidscript = 0
        counter_python = 0
        counter_p4a = 0
        counter_pys60 = 0
        counter_html = 0
        counter_css = 0
        counter_js = 0
        counter_jq = 0
        counter_angular = 0
        counter_sql = 0
        counter_linux = 0

        for url, count in json.loads(i['urls']).iteritems():
            if url.startswith('/docs/android/'):
                counter_android += count
            elif url.startswith('/docs/java/'):
                counter_java += count
            elif url.startswith('/docs/droidscript/'):
                counter_droidscript += count
            elif url.startswith('/docs/python/'):
                counter_python += count
            elif url.startswith('/docs/p4a/'):
                counter_p4a += count
            elif url.startswith('/docs/pys60/'):
                counter_pys60 += count
            elif url.startswith('/docs/html/'):
                counter_html += count
            elif url.startswith('/docs/css/'):
                counter_css += count
            elif url.startswith('/docs/js/'):
                counter_js += count
            elif url.startswith('/docs/jq/'):
                counter_jq += count
            elif url.startswith('/docs/angular/'):
                counter_angular += count
            elif url.startswith('/docs/sql/'):
                counter_sql += count
            elif url.startswith('/docs/linux/'):
                counter_linux += count

        data_android_append(counter_android)
        data_java_append(counter_java)
        data_droidscript_append(counter_droidscript)
        data_python_append(counter_python)
        data_p4a_append(counter_p4a)
        data_pys60_append(counter_pys60)
        data_html_append(counter_html)
        data_css_append(counter_css)
        data_js_append(counter_js)
        data_jq_append(counter_jq)
        data_angular_append(counter_angular)
        data_sql_append(counter_sql)
        data_linux_append(counter_linux)

    return JsonResponse({
        'labels': times,
        'data_android': data['android'],
        'data_java': data['java'],
        'data_droidscript': data['droidscript'],
        'data_python': data['python'],
        'data_p4a': data['p4a'],
        'data_pys60': data['pys60'],
        'data_html': data['html'],
        'data_css': data['css'],
        'data_js': data['js'],
        'data_jq': data['jq'],
        'data_angular': data['angular'],
        'data_sql': data['sql'],
        'data_linux': data['linux'],
    })
