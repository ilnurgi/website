# coding: utf-8

import datetime

import pymongo
from pymongo.mongo_client import MongoClient

from django.shortcuts import render_to_response
from django.conf import settings
import logging

logger = logging.getLogger(__name__)

def view(request):

    mongo_client = MongoClient(
        settings.DATABASE_MONGO['host'],
        int(settings.DATABASE_MONGO['port']))

    db = mongo_client[
        settings.DATABASE_MONGO['arduino_db_name']]

    if 'light' in request.GET:

        try:
            latest_doc = list(db.light.find().sort('date', -1).limit(1))[0]
        except IndexError:
            db.light.inser_one(
                {
                    'date': datetime.datetime.now(),
                    'light': request.GET['light']
                })
        else:
            if latest_doc['light'] != request.GET['light']:
                db.light.inser_one(
                    {
                        'date': datetime.datetime.now(),
                        'light': request.GET['light']
                    })

    return render_to_response(
        'arduino.html',
        context={
            'data': db.light.find()
        })
