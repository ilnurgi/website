# coding: utf-8

import datetime

import psutil

from pymongo import MongoClient

from django.conf import settings
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """
    собираем инофрмацию по загруженности сервера
    """

    def handle(self, *args, **options):

        mongo_client = MongoClient(
            settings.DATABASE_MONGO['host'],
            int(settings.DATABASE_MONGO['port']))

        self.db = mongo_client[
            settings.DATABASE_MONGO['cpu_average_db_name']]

        self.collection_average_minute = self.db.average_minute
        self.collection_average_hour = self.db.average_hour

        now = datetime.datetime.now()
        last_hour = now.hour
        while True:
            percent = psutil.cpu_percent(interval=60)
            now = datetime.datetime.now()

            self.collection_average_minute.insert_one({
                'percent': percent,
                'date': now
            })

            if last_hour != now.hour:
                self.calculate_hour(now)
                self.drop_old(now)
                last_hour = now.hour

    def calculate_hour(self, date):
        _date = date - datetime.timedelta(hours=1)
        rows = self.collection_average_minute.find({
            'date': {
                '$gte': _date
            }
        })

        if rows.count():
            self.collection_average_hour.insert_one({
                'date': _date,
                'percent': sum((i['percent'] for i in rows))/rows.count()
            })

    def drop_old(self, now):
        self.collection_average_hour.delete_many({
            'date': {
                '$lt': now - datetime.timedelta(days=3),
            }
        })
        self.collection_average_minute.delete_many({
            'date': {
                '$lt': now - datetime.timedelta(days=3),
            }
        })
