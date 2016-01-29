# coding: utf-8

import pymongo
import datetime

mongo_client = pymongo.MongoClient('localhost', 27017)

db = mongo_client['nginx_access']

for i in db.month_report.find().sort('date'):
    print i['date']
    # db.month_report.update_one(
    #     {
    #         '_id': i['_id']
    #     }, {
    #         '$set': {
    #             'date': i['date'].replace(month=i['date'].month + 1)
    #         }
    #     }
    # )
