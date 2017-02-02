# coding: utf-8

import datetime
import json
import tempfile

from django.conf import settings
from django.core.management import call_command
from django.core.urlresolvers import reverse
from django.test import TestCase

from pymongo import MongoClient


class TestParsingNginxAccess(TestCase):

    def tearDown(self):
        self.mongo_client.drop_database(self.mongo_db)

    def setUp(self):

        self.mongo_client = MongoClient(
            settings.DATABASE_MONGO['host'],
            int(settings.DATABASE_MONGO['port']))

        self.mongo_db = self.mongo_client[
            settings.DATABASE_MONGO['nginx_access_db_name']]
        self.collection_log = self.mongo_db.log
        self.collection_month_report = self.mongo_db.month_report

    def test_data_week(self):
        """
        посещения за неделю, без учета ботов
        :return:
        """
        bots_input = [
            '82.117.240.{} - - '
            '[11/Nov/2015:06:30:01 -0500] '
            '"GET /docs/python/modules_user/pyqt/qtgui/qwqweqew.html HTTP/1.1" '
            '200 9078 '
            '"https://www.google.com.ua/" {}'.format(i, ua)

            for i, ua in enumerate((

                '"Mozilla/5.0 (compatible; MJ12bot/v1.4.5; '
                'http://www.majestic12.co.uk/bot.php?+) "',

                '"Mozilla/5.0 (compatible; Baiduspider/2.0; '
                '+http://www.baidu.com/search/spider.html) "',

                '"Mozilla/5.0 (compatible; Googlebot/2.1; '
                '+http://www.google.com/bot.html) "',

                '"Mozilla/5.0 (compatible; YandexBot/3.0; '
                '+http://yandex.com/bots) "',

                '"Mozilla/5.0 (compatible; bingbot/2.0; '
                '+http://www.bing.com/bingbot.htm) "',

                '"Riddler (http://riddler.io/about) "',

                '"Mozilla/5.0 (compatible; AhrefsBot/5.1; "'
                '"+http://ahrefs.com/robot/) "',

                '"Mozilla/5.0 (compatible; SemrushBot/1.1~bl; '
                '+http://www.semrush.com/bot.html) "',

                '"Mozilla/5.0 (compatible; archive.org_bot '
                '+http://www.archive.org/details/archive.org_bot)"'
            ))]
        inp = (
            # пользовательский просмотр
            '82.117.241.1 - - '
            '[11/Nov/2015:06:30:01 -0500] '
            '"GET /docs/python/modules_user/pyqt/qtgui/qwidget.html HTTP/1.1" '
            '200 9078 '
            '"https://www.google.com.ua/" '
            '"Mozilla/5.0 (Windows NT 6.1; WOW64)"',

            # пользовательский просмотр
            '82.117.241.2 - - '
            '[11/Nov/2015:06:30:02 -0500] '
            '"GET /docs/python/modules_user/pyqt/qtgui/qwidget.html HTTP/1.1" '
            '200 9078 '
            '"https://www.google.com.ua/" '
            '"Mozilla/5.0 (Windows NT 6.1; WOW64)"',

            # пользовательский просмотр
            '82.117.241.3 - - '
            '[11/Nov/2015:06:30:03 -0500] '
            '"GET /docs/python/modules_user/pyqt/qtgui/qwidget.html HTTP/1.1" '
            '200 9078 '
            '"https://www.google.com.ua/" '
            '"Mozilla/5.0 (Windows NT 6.1; WOW64)"',

            # пользовательский просмотр
            '82.117.241.3 - - '
            '[11/Nov/2015:06:30:04 -0500] '
            '"GET /blog/python/modules_user/pyqt/qtgui/qwidget.html HTTP/1.1" '
            '200 9078 '
            '"https://www.google.com.ua/" '
            '"Mozilla/5.0 (Windows NT 6.1; WOW64)"',

            # пользовательский просмотр
            '82.117.241.3 - - '
            '[12/Nov/2015:06:30:04 -0500] '
            '"GET /blog/python/modules_user/pyqt/qtgui/qwidget.html HTTP/1.1" '
            '200 9078 '
            '"https://www.google.com.ua/" '
            '"Mozilla/5.0 (Windows NT 6.1; WOW64)"',

            # пользовательский просмотр
            '82.117.241.3 - - '
            '[12/Nov/2015:06:30:04 -0500] '
            '"GET /docs/python/modules_user/pyqt/qtgui/qwidget.html HTTP/1.1" '
            '200 9078 '
            '"https://www.google.com.ua/" '
            '"Mozilla/5.0 (Windows NT 6.1; WOW64)"',
        ) + tuple(bots_input)

        input_file = tempfile.TemporaryFile()
        input_file.write('\n'.join(inp))
        input_file.seek(0)

        now = datetime.datetime(2015, 11, 12, 12, 12, 12)
        call_command(
            'parse_nginx_access',
            input_file=input_file,
            date_today=now
        )

        input_file = tempfile.TemporaryFile()
        input_file.write('\n'.join(inp))
        input_file.seek(0)

        call_command(
            'parse_nginx_access',
            input_file=input_file,
            date_today=now + datetime.timedelta(days=1)
        )

        response = self.client.get(
            reverse("metrics:data_week"),
            {
                "date_now": (
                    now + datetime.timedelta(days=3)
                ).strftime("%Y.%m.%d %H.%M.%S")
            })
        self.assertEqual(response.status_code, 200)
        result = json.loads(response.content)

        self.assertSequenceEqual(result['ip_count_uniq'], [3, 1])
        self.assertSequenceEqual(result['ip_count'], [4, 2])
        self.assertSequenceEqual(result['blog_all_count'], [1, 1])
        self.assertSequenceEqual(result['doc_all_count'], [3, 1])
        self.assertSequenceEqual(result['labels'], ["11.11.2015", "12.11.2015"])
