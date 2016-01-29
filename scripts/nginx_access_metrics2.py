# coding: utf-8

import pymongo
import datetime

from metrics.management.commands.parse_nginx_access import Command


mongo_client = pymongo.MongoClient('localhost', 27017)

db = mongo_client['nginx_access']

print db.month_report.count()
command = Command()
command.today = datetime.datetime(2016, 1, 1, 0, 0, 0)
command.collection_log = db.log
command.collection_month_report = db.month_report
# command.calculate_for_month()

print db.log.count()
# print db.log.delete_many(
#     {
#         'date': {
#             '$lt': datetime.datetime(2016, 1, 1, 0, 0, 0)
#         }
#     })
print db.log.count()
