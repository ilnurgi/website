# coding: utf-8

import datetime

import pymongo
from pymongo.mongo_client import MongoClient

from django.shortcuts import render_to_response
from django.conf import settings


def view(request):
    print request.POST
    return render_to_response('arduino.html')
