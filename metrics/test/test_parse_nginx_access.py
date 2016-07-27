# coding: utf-8

import datetime
import json
import tempfile

from pymongo import MongoClient

from django.conf import settings
from django.core.management import call_command
from django.test import TestCase


class TestParsingNginxAccess(TestCase):

    def tearDown(self):
        self.mongo_client.drop_database(self.mongo_db)

    def setUp(self):

        self.mongo_client = MongoClient(
            settings.DATABASE_MONGO['host'],
            int(settings.DATABASE_MONGO['port']))

        self.mongo_db = self.mongo_client[
            settings.DATABASE_MONGO['nginx_access_db_name'] + '_test']
        self.collection_log = self.mongo_db.log
        self.collection_month_report = self.mongo_db.month_report

    def test_parsing(self):
        """
        тестируем парсинг простой, все записи должны попасть в коллекцию
        """
        inp = (
            '82.117.240.50 - - '
            '[11/Nov/2015:06:30:01 -0500] '
            '"GET /docs/python/modules_user/pyqt/qtgui/qwidget.html HTTP/1.1" '
            '200 9078 '
            '"https://www.google.com.ua/" '
            '"Mozilla/5.0 (Windows NT 6.1; WOW64)"',

            '82.117.240.50 - - '
            '[11/Nov/2015:06:30:01 -0500] '
            '"GET /docs/python/_static/classic.css HTTP/1.1" '
            '200 4403 '
            '"http://www.ilnurgi1.ru/docs/python/modules_user/pyqt/qtgui/'
            'qwidget.html" '
            '"Mozilla/5.0 (Windows NT 6.1; WOW64)"',

            '212.193.117.227 - - '
            '[11/Nov/2015:05:21:19 -0400] '
            '"GET / HTTP/1.1" '
            '200 431 '
            '"" '
            '"Mozilla/5.0 (compatible; statdom.ru/Bot; '
            '+http://statdom.ru/bot.html)"',

            '212.193.117.227 - - '
            '[11/Nov/2015:05:21:22 -0400] '
            '"GET /favicon.ico HTTP/1.1" '
            '404 961 '
            '"" '
            '"Mozilla/5.0 (compatible; statdom.ru/Bot; '
            '+http://statdom.ru/bot.html)"',

            '148.251.223.21 - - '
            '[11/Nov/2015:14:23:48 -0400] '
            '"GET /robots.txt HTTP/1.1" '
            '404 957 '
            '"" '
            '"Mozilla/5.0 (compatible; openstat.ru/Bot)"',

            '61.160.247.11'
            ' - root '
            '[11/Nov/2015:00:50:03 -0400] '
            '"GET /manager/html HTTP/1.1" '
            '404 2047 '
            '"-" '
            '"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1;)"'

        )

        input_file = tempfile.TemporaryFile()
        input_file.write('\n'.join(inp))
        input_file.seek(0)

        call_command(
            'parse_nginx_access',
            mongo_db=self.mongo_db,
            input_file=input_file,
            date_today=datetime.datetime(2015, 11, 12, 0, 0, 0)
        )

        # 3 - записей статики
        self.assertEqual(self.collection_log.count(), len(inp) - 3)

    def test_log_today(self):
        """
        в лог должны попасть только сегоднящние записи
        """
        inp = (
            '82.117.240.50 - - '
            '[11/Nov/2015:06:30:01 -0500] '
            '"GET /docs/python/modules_user/pyqt/qtgui/qwidget.html HTTP/1.1" '
            '200 9078 '
            '"https://www.google.com.ua/" '
            '"Mozilla/5.0 (Windows NT 6.1; WOW64)"',

            '82.117.240.50 - - '
            '[11/Nov/2015:06:30:01 -0500] '
            '"GET /docs/python/_static/classic.css HTTP/1.1" '
            '200 4403 '
            '"http://www.ilnurgi1.ru/docs/python/modules_user/pyqt/qtgui/'
            'qwidget.html" '
            '"Mozilla/5.0 (Windows NT 6.1; WOW64)"')

        input_file = tempfile.TemporaryFile()
        input_file.write('\n'.join(inp))
        input_file.seek(0)

        call_command(
            'parse_nginx_access',
            mongo_db=self.mongo_db,
            input_file=input_file,
            date_today=datetime.datetime(2015, 11, 13, 12, 12, 12)
        )

        self.assertEqual(self.collection_log.count(), 0)

    def test_calculate_month(self):
        """
        аккумулирование за месяц
        """
        inp = (
            '82.117.240.50 - - '
            '[11/Nov/2015:06:30:01 -0500] '
            '"GET /docs/python/modules_user/pyqt/qtgui/qwidget.html HTTP/1.1" '
            '200 9078 '
            '"https://www.google.com.ua/" '
            '"Mozilla/5.0 (Windows NT 6.1; WOW64)"',

            '82.117.240.51 - - '
            '[11/Nov/2015:06:30:01 -0500] '
            '"GET /docs/python/modules_user/pyqt/qtgui/qwidget.html HTTP/1.1" '
            '200 9078 '
            '"https://www.google.com.ua/" '
            '"Mozilla/5.0 (Windows NT 6.1; WOW64)"',

            '82.117.240.51 - - '
            '[11/Nov/2015:06:30:01 -0500] '
            '"GET /docs/python/modules_user/pyqt/qtgui/qwidget.html HTTP/1.1" '
            '200 9078 '
            '"http://www.ilnurgi1.ru/docs/python/index.html" '
            '"Mozilla/5.0 (Windows NT 6.1; WOW64)"',

            '82.117.240.51 - - '
            '[11/Nov/2015:06:30:01 -0500] '
            '"GET /docs/python/_static/classic.css HTTP/1.1" '
            '200 4403 '
            '"http://www.ilnurgi1.ru/docs/python/modules_user/pyqt/qtgui/'
            'qwidget.html" '
            '"Mozilla/5.0 (Windows NT 6.1; WOW64)"')

        input_file = tempfile.TemporaryFile()
        input_file.write('\n'.join(inp))
        input_file.seek(0)

        call_command(
            'parse_nginx_access',
            mongo_db=self.mongo_db,
            input_file=input_file,
            date_today=datetime.datetime(2015, 11, 12, 12, 12, 12)
        )

        # 1 - статика
        self.assertEqual(self.collection_log.count(), len(inp) - 1)

        inp = (
            '82.117.240.50 - - '
            '[01/Dec/2015:06:30:01 -0500] '
            '"GET /docs/python/modules_user/pyqt/qtgui/qwidget.html HTTP/1.1" '
            '200 9078 '
            '"https://www.google.com.ua/" '
            '"Mozilla/5.0 (Windows NT 6.1; WOW64)"',

            '82.117.240.50 - - '
            '[01/Dec/2015:06:30:01 -0500] '
            '"GET /docs/python/_static/classic.css HTTP/1.1" '
            '200 4403 '
            '"http://www.ilnurgi1.ru/docs/python/modules_user/pyqt/qtgui/'
            'qwidget.html" '
            '"Mozilla/5.0 (Windows NT 6.1; WOW64)"')

        input_file = tempfile.TemporaryFile()
        input_file.write('\n'.join(inp))
        input_file.seek(0)

        # загрузили данные, теперь соберем за месяц
        call_command(
            'parse_nginx_access',
            mongo_db=self.mongo_db,
            input_file=input_file,
            date_today=datetime.datetime(2015, 12, 1, 12, 12, 12)
        )

        self.assertEqual(self.collection_month_report.count(), 1)
        self.assertEqual(self.collection_log.count(), 0)

        result = self.collection_month_report.find_one()

        # всего 5 просмотров, но 3 статики
        self.assertEqual(result['ip_count'], 3)

        self.assertEqual(result['ip_uniq_count'], 2)

        urls = json.loads(result['urls'])
        self.assertEqual(
            urls['/docs/python/modules_user/pyqt/qtgui/qwidget.html'],
            3)

        urls_from = json.loads(result['urls_from'])

        self.assertEqual(
            urls_from['https://www.google.com.ua/'],
            2)
        self.assertNotIn(
            'http://www.ilnurgi1.ru/docs/python/index.html',
            urls_from,
        )

        user_agents = json.loads(result['user_agents'])
        self.assertEqual(
            user_agents['Mozilla/5.0 (Windows NT 6.1; WOW64)'],
            3)
