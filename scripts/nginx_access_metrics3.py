# coding: utf-8

import datetime
import json
import os
import re

import pymongo

mongo_client = pymongo.MongoClient('localhost', 27017)

db = mongo_client['nginx_access']
db.log.drop()
db.month_report.drop()

log_re = re.compile(
    ur'^\s*(?P<ip_address>\d+\.\d+\.\d+\.\d+) - \S+ '
    ur'\[(?P<date>\S+) \S+\] '
    ur'"(?P<method>\w+) (?P<url>\S+) \S+" '
    ur'(?P<status>\d+) (?P<size>\d+) '
    ur'"(?P<url_from>\S*)" '
    ur'"(?P<user_agent>.*)"\s*$'
)

LOG_PATH = os.path.join(
    os.path.dirname(
        os.path.dirname(__file__)),
    u'logs')


def parse(file_path):
    print u'parse:', file_path

    for line in open(file_path):
        data = log_re.match(line[:-1])
        if not data:
            continue

        data = data.groupdict()

        if (
                data['url'].endswith('.css') or
                data['url'].endswith('.php') or
                data['url'].endswith('.js')):
            continue

        data['status'] = int(data['status'])
        data['date'] = datetime.datetime.strptime(
            data['date'],
            '%d/%b/%Y:%H:%M:%S')
        db.log.insert_one(data)


def calculate_for_month(date_start):
    def get_logs(date_start, date_end):
        for i in xrange(31*2):
            _date_start = date_start + datetime.timedelta(hours=12*i)
            _date_end = date_start + datetime.timedelta(hours=12*(i+1))
            for log in db.log.find(
                {
                    'date': {
                        '$gte': _date_start,
                        '$lt': _date_end
                    }
                }):
                yield log
            if _date_end == date_end:
                break

    print u'calculate_for_month'

    today = date_start
    january = today.month == 1

    date_start = datetime.datetime(
        today.year - (1 if january else 0),
        12 if january else today.month - 1,
        1,
        0, 0, 0)

    december = date_start.month == 12
    date_end = datetime.datetime(
        date_start.year + (1 if december else 0),
        1 if december else date_start.month + 1,
        1,
        0, 0, 0)
    print u'date_start = {0}'.format(date_start)
    print u'date_end = {0}'.format(date_end)

    urls = {}
    urls_from = {}
    user_agents = {}
    ip_count = 0
    ip_uniq_count = 0
    ip_set = set()

    result = {
        'date': date_end,
        'urls': urls,
        'urls_from': urls_from,
        'user_agents': user_agents,
    }

    for log in get_logs(date_start, date_end):
        url = log['url']
        urls[url] = urls.setdefault(url, 0) + 1

        url_from = log['url_from']

        if (not url_from.startswith('http://ilnurgi1.ru') or
                not url_from.startswith('http://ilnurgi1.ru')):
            urls_from[url_from] = urls_from.setdefault(url_from, 0) + 1

        user_agent = log['user_agent']
        user_agents[user_agent] = user_agents.setdefault(user_agent, 0) + 1

        ip = log['ip_address']
        ip_count += 1
        if ip not in ip_set:
            ip_set.add(ip)
            ip_uniq_count += 1

    result['urls'] = json.dumps(result['urls'])
    result['urls_from'] = json.dumps(result['urls_from'])
    result['user_agents'] = json.dumps(result['user_agents'])
    result['ip_count'] = ip_count
    result['ip_uniq_count'] = ip_uniq_count

    db.month_report.insert_one(result)

for f in os.listdir(LOG_PATH):
    f_p = os.path.join(LOG_PATH, f)
    if os.path.isfile(f_p) and f.startswith('nginx_access'):
        parse(f_p)

dates = (
    datetime.datetime(2015, 7, 1, 0, 0, 0),
    datetime.datetime(2015, 8, 1, 0, 0, 0),
    datetime.datetime(2015, 9, 1, 0, 0, 0),
    datetime.datetime(2015, 10, 1, 0, 0, 0),
    datetime.datetime(2015, 11, 1, 0, 0, 0),
    datetime.datetime(2015, 12, 1, 0, 0, 0),
    datetime.datetime(2016, 1, 1, 0, 0, 0),
    datetime.datetime(2016, 2, 1, 0, 0, 0),
    datetime.datetime(2016, 3, 1, 0, 0, 0),
)
for date in dates:
    calculate_for_month(date)
