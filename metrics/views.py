# coding: utf-8

import datetime
import json

import pymongo

from django.conf import settings
from django.http import JsonResponse
from django.views.generic import TemplateView

from application.views import ConspectsMixin


class HomePage(ConspectsMixin, TemplateView):

    template_name = 'base_metrics.html'
    active_page_sub = ''

    def get_context_data(self, **kwargs):
        context = super(HomePage, self).get_context_data(**kwargs)
        context['active_page'] = 'metrics'
        context['active_page_sub'] = self.active_page_sub
        return context


class System(HomePage):

    template_name = 'metrics_system.html'
    active_page_sub = "system"


class Visiters(HomePage):

    template_name = 'metrics_visiters.html'
    active_page_sub = "visiters"


class URLS(HomePage):

    template_name = 'metrics_urls.html'
    active_page_sub = "urls"

    def get_context_data(self, **kwargs):
        context = super(URLS, self).get_context_data(**kwargs)

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
    active_page_sub = "urls_from"

    def get_context_data(self, **kwargs):
        context = super(URLSFrom, self).get_context_data(**kwargs)

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
    active_page_sub = "user_agents"

    def get_context_data(self, **kwargs):
        context = super(UserAgents, self).get_context_data(**kwargs)

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


def get_db(db_name):
    """
    возвращаем БД

    :param db_name:
    :return:
    """
    mongo_client = pymongo.MongoClient(
        settings.DATABASE_MONGO['host'],
        int(settings.DATABASE_MONGO['port']))

    return mongo_client[db_name]


def cpu_data(request):

    db = get_db(settings.DATABASE_MONGO['cpu_average_db_name'])

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
    db = get_db(settings.DATABASE_MONGO['cpu_average_db_name'])

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
    db = get_db(settings.DATABASE_MONGO['mem_average_db_name'])

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
    db = get_db(settings.DATABASE_MONGO['mem_average_db_name'])

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


def get_records(collection, date_start, date_end):
    """
    итератор, возвращает данные из коллекции, делая запрос по дням

    :param collection:

    :param date_start: начало среза
    :type date_start: datetime.datetime

    :param date_end: конец среза
    :type date_end: datetime.datetime

    :return:
    """
    delta = date_end - date_start
    for i in xrange(delta.days + 1):
        _date_start = date_start + datetime.timedelta(days=i)
        _date_end = date_start + datetime.timedelta(days=i + 1)
        for record in collection.find(
                {
                    'date': {
                        '$gte': _date_start,
                        '$lt': _date_end
                    }
                }).sort('date'):
            yield record
        if _date_end == date_end:
            break


def data_month(requset):
    """
    информация по посещаемости по месяцам
    возвращает жсон,
    {
        'labels': список дат
        'ip_count': список количеств ипи по дням
        'ip_count_uniq': список количеств уникальных ипи по дням
        'doc_all_count': список количеств просмотров конспектов по дням
        'blog_all_count': список количеств просмотров блога по дням
    }

    :param requset:
    :return:
    """
    db = get_db(settings.DATABASE_MONGO['nginx_access_db_name'])

    times = []
    times_append = times.append

    _ip_data = []
    ip_data_append = _ip_data.append

    _ip_uniq_data = []
    ip_uniq_data_append = _ip_uniq_data.append

    _docs_data = []
    docs_data_append = _docs_data.append

    _blog_data = []
    blog_data_append = _blog_data.append

    for i in db.month_report.find().sort('date'):
        times_append(i['date'].strftime('%d.%m.%Y'))
        ip_data_append(i['ip_count'])
        ip_uniq_data_append(i['ip_uniq_count'])

        docs_counter = 0
        blog_counter = 0
        for url, count in json.loads(i['urls']).iteritems():
            if url.startswith('/docs/'):
                docs_counter += count
            elif url.startswith('/blog/'):
                blog_counter += count
        docs_data_append(docs_counter)
        blog_data_append(blog_counter)

    return JsonResponse({
        'labels': times,
        'ip_count': _ip_data,
        'ip_count_uniq': _ip_uniq_data,
        'doc_all_count': _docs_data,
        'blog_all_count': _blog_data,
    })


def data_week(requset):
    """
    информация по посещаемости за последнюю неделю
    возвращает жсон,
    {
        'labels': список дат
        'ip_count': список количеств ипи по дням
        'ip_count_uniq': список количеств уникальных ипи по дням
        'doc_all_count': список количеств просмотров конспектов по дням
        'blog_all_count': список количеств просмотров блога по дням
    }

    :param requset:
    :return:
    """
    db = get_db(settings.DATABASE_MONGO['nginx_access_db_name'])

    times = []
    times_append = times.append

    _ip_data = []
    ip_data_append = _ip_data.append

    _ip_uniq_data = []
    ip_uniq_data_append = _ip_uniq_data.append

    _docs_all_data = []
    docs_all_data_append = _docs_all_data.append

    _blog_all_data = []
    blog_all_data_append = _blog_all_data.append

    date_now = datetime.datetime.now()
    # date_now = datetime.datetime.now() - datetime.timedelta(days=15)
    date_end = datetime.datetime.combine(
        date_now.date() - datetime.timedelta(days=1),
        datetime.time(23, 59, 59)
    )
    date_start = datetime.datetime.combine(
        (date_end - datetime.timedelta(weeks=1)).date(),
        datetime.time(0, 0, 0)
    )

    last_date = None
    ip_count = 0
    ip_uniq_count_set = set()
    docs_all_count = 0
    blog_all_count = 0

    for record in get_records(db.log, date_start=date_start, date_end=date_end):

        record_date = record['date'].date()

        if not last_date:
            last_date = record_date
        elif last_date != record_date:
            times_append(record_date.strftime('%d.%m.%Y'))
            ip_data_append(ip_count)
            ip_uniq_data_append(len(ip_uniq_count_set))
            docs_all_data_append(docs_all_count)
            blog_all_data_append(blog_all_count)

            last_date = record_date
            ip_count = 0
            ip_uniq_count_set.clear()
            docs_all_count = 0
            blog_all_count = 0
        else:
            ip_count += 1
            ip_uniq_count_set.add(record['ip_address'])
            if record['url'].startswith('/docs/'):
                docs_all_count += 1
            elif record['url'].startswith('/blog/'):
                blog_all_count += 1

    return JsonResponse({
        'labels': times,
        'ip_count': _ip_data,
        'ip_count_uniq': _ip_uniq_data,
        'doc_all_count': _docs_all_data,
        'blog_all_count': _blog_all_data,
    })


def docs_data_all(request):
    db = get_db(settings.DATABASE_MONGO['nginx_access_db_name'])

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
