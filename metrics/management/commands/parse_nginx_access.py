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
        logger.debug(u'='*80)

        mongo_client = MongoClient(
            settings.DATABASE_MONGO['host'],
            int(settings.DATABASE_MONGO['port']))

        self.db = mongo_client[
            options.get(
                'mongo_db_name',
                settings.DATABASE_MONGO['nginx_access_db_name'])]

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
        logger.debug(u'today={0}'.format(self.today))
        date_start = datetime.datetime.combine(
            self.today - datetime.timedelta(days=1),
            datetime.time(0, 0, 0))
        date_end = datetime.datetime.combine(
            date_start,
            datetime.time(23, 59, 59))
        logger.debug(u'date_start={0}'.format(date_start))
        logger.debug(u'date_end={0}'.format(date_end))

        log_file_path = os.path.join(settings.LOG_PATH, u'nginx_access.log')
        new_log_file_path = (
            options['log_file_path']
            if options['log_file_path']
            else log_file_path.replace(
                u'.log', u'_{0}.log'.format(date_start.date())))
        logger.debug(u'log_file_path={0}'.format(log_file_path))
        logger.debug(u'new_log_file_path={0}'.format(new_log_file_path))

        if not any(
                (options.get('input_file', None),
                 options.get('log_file_path', None))):
            logger.debug(u'os rename')
            try:
                os.rename(log_file_path, new_log_file_path)
            except Exception as err:
                logger.debug(err)
                raise

            logger.debug(u'nginx restart')
            result = subprocess.call([u'service', u'nginx', u'restart'])
            if result:
                logger.debug(result)

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

                if (
                        data['url'].endswith('.css') or
                        data['url'].endswith('.php') or
                        data['url'].endswith('.ico') or
                        data['url'].endswith('.txt') or
                        data['url'].endswith('.js')):
                    logger.debug(u'static: {0}'.format(data['url']))
                    continue

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
        logger.debug(u'calculate_for_month')

        today = self.today
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
        logger.debug(u'date_start = {0}'.format(date_start))
        logger.debug(u'date_end = {0}'.format(date_end))

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

        exclude_urls = {
            'http://ilnurgi1.ru', 'http://www.ilnurgi1.ru', 'ilnurgi1.ru',
        }

        for log in self.get_logs(date_start, date_end):
            url_from = log['url_from']
            user_agent = log['user_agent']
            url = log['url']
            ip = log['ip_address']

            user_agents[user_agent] = (
                user_agents.setdefault(user_agent, 0) + 1)

            if any(excl_ua in user_agent
                   for excl_ua in settings.EXCLUDE_USER_AGENTS):
                # это поисковый бот, его мы не учитываем
                # но сохраним юзер агента
                continue

            # количесвто посещений урла
            urls[url] = urls.setdefault(url, 0) + 1

            # если пришли не с нашей старницы
            if not any(map(url_from.startswith, exclude_urls)):
                urls_from[url_from] = urls_from.setdefault(url_from, 0) + 1

            # количество просмотров с айпи
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

    def get_logs(self, date_start, date_end):
        for i in xrange(40):
            _date_start = date_start + datetime.timedelta(days=i)
            _date_end = date_start + datetime.timedelta(days=i+1)
            for log in self.collection_log.find(
                {
                    'date': {
                        '$gte': _date_start,
                        '$lt': _date_end
                    }
                }):
                yield log
            if _date_end == date_end:
                break
