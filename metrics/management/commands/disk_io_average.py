# coding: utf-8

import datetime
import time

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
            settings.DATABASE_MONGO['disk_io_db_name']]

        self.collection_read = self.db.read
        self.collection_write = self.db.write

        stat = psutil.disk_io_counters()
        now_last = datetime.datetime.now()

        read_bytes_last = stat.read_bytes
        write_bytes_last = stat.write_bytes

        while True:
            time.sleep(10)

            stat = psutil.disk_io_counters()
            now = datetime.datetime.now()

            self.collection_read.insert_one({
                'read_bytes': stat.read_bytes - read_bytes_last,
                'date': now})

            self.collection_write.insert_one({
                'write_bytes': stat.write_bytes - write_bytes_last,
                'date': now})

            read_bytes_last = stat.read_bytes
            write_bytes_last = stat.write_bytes

            if now.month != now_last.month:
                self.collection_read.delete_many({
                    'date': {
                        '$lt': now_last,
                    }
                })
                self.collection_write.delete_many({
                    'date': {
                        '$lt': now_last,
                    }
                })
                now_last = now
