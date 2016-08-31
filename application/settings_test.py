# coding: utf-8

from .settings import *

DATABASE_MONGO = {
    'host': 'localhost',
    'port': '27017',
    'nginx_access_db_name': 'nginx_access_test',
    'cpu_average_db_name': 'cpu_average_test',
    'mem_average_db_name': 'mem_average_test',
    'disk_io_db_name': 'disk_io_average_test',
}
