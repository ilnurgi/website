# coding: utf-8

import datetime
import json
import logging
import os
import re
import subprocess

from pymongo import MongoClient

from django.conf import settings
from django.core.management.base import BaseCommand

logger = logging.getLogger('parse_nginx_access')


class Command(BaseCommand):
    """
    парсим nginx_access.log
    """

    date_format = '%Y.%m.%d'

    def add_arguments(self, parser):
        parser.add_argument(
            '-d', '--date', dest='date', default=None, help=self.date_format)
        parser.add_argument(
            '-l', '--log', dest='log_file_path', default=None)

    def handle(self, *args, **options):

        if 'mongo_db' not in options:
            mongo_client = MongoClient(
                settings.DATABASE_MONGO['host'],
                int(settings.DATABASE_MONGO['port']))

            self.db = mongo_client[
                options.get(
                    'mongo_db_name',
                    settings.DATABASE_MONGO['nginx_access_db_name'])]
        else:
            self.db = options['mongo_db']

        self.collection_log = self.db.log
        self.collection_month_report = self.db.month_report

        self.log_re = re.compile(
            ur'^\s*(?P<ip_address>\d+\.\d+\.\d+\.\d+) - \S+ '
            ur'\[(?P<date>\S+) \S+\] '
            ur'"(?P<method>\w+) (?P<url>\S+) \S+" '
            ur'(?P<status>\d+) (?P<size>\d+) '
            ur'"(?P<url_from>\S*)" '
            ur'"(?P<user_agent>.*)"\s*$'
        )

        self.today = options.get(
            'date_today',
             datetime.datetime.strptime(options['date'], self.date_format)
                if options['date'] else datetime.datetime.now())
        date_start = datetime.datetime.combine(
            self.today - datetime.timedelta(days=1),
            datetime.time(0, 0, 0))
        date_end = datetime.datetime.combine(
            date_start,
            datetime.time(23, 59, 59))

        log_file_path = os.path.join(settings.LOG_PATH, u'nginx_access.log')
        new_log_file_path = (
            options['log_file_path']
            if options['log_file_path']
            else log_file_path.replace(
                u'.log', u'_{0}.log'.format(date_start.date())))

        if 'input_file' not in options or 'log_file_path' not in options:
            os.rename(log_file_path, new_log_file_path)

            subprocess.call([u'service', u'nginx', u'restart'])

        file_obj = options.get(
            'input_file',
            None)
        if file_obj is None:
            file_obj = open(new_log_file_path)

        with file_obj as log_file:
            for log in log_file:
                data = self.log_re.match(log)
                if not data:
                    logger.debug(log)
                    continue

                data = data.groupdict()
                data['status'] = int(data['status'])
                data['date'] = datetime.datetime.strptime(
                    data['date'],
                    '%d/%b/%Y:%H:%M:%S')

                if not (date_start < data['date'] < date_end):
                    continue

                self.collection_log.insert_one(data)

        if self.today.day == 1:
            self.calculate_for_month()
            self.drop()

    def calculate_for_month(self):

        today = self.today
        january = today.month == 1

        date_start = datetime.datetime(
            today.year - (1 if january else 0),
            12 if january else today.month - 1,
            1,
            0, 0, 0)

        december = today.month == 12
        date_end = datetime.datetime(
            date_start.year + (1 if december else 0),
            1 if december else date_start.month + 1,
            1,
            0, 0, 0)

        urls = {}
        urls_from = {}
        user_agents = {}
        ip_count = 0
        ip_uniq_count = 0
        ip_set = set()

        result = {
            'date': date_start,
            'urls': urls,
            'urls_from': urls_from,
            'user_agents': user_agents,
        }

        logs = self.collection_log.find(
            {
                'date': {
                    '$gte': date_start,
                    '$lt': date_end
                }
            })

        for log in logs:
            url = log['url']
            urls[url] = urls.setdefault(url, 0) + 1

            url_from = log['url_from']
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

        self.collection_month_report.insert_one(result)

    def drop(self):
        self.collection_log.drop()
