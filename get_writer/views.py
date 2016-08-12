# coding: utf-8

import datetime
import pymongo

from django.conf import settings
from django.shortcuts import render_to_response


def get_writer(request):

    mongo_client = pymongo.MongoClient(
        settings.DATABASE_MONGO['host'],
        int(settings.DATABASE_MONGO['port']))

    db = mongo_client['get_writer']
    collection = db.collection

    if request.GET:
        now = datetime.datetime.now()
        record = {key: value for key, value in request.GET.items()}
        record['date'] = now
        collection.insert_one(record)
        collection.delete_many(
            {
                'date': {
                    '$lt': now - datetime.timedelta(days=1),
                },
            },
        )

    return render_to_response(
        'get_writer.html',
        {'records': collection.find().sort('date', -1)}
    )
