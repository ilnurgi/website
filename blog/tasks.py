# coding: utf-8

import datetime

from celery.task import task

from django.core.mail import mail_admins


@task()
def send_email_notification(url):
    mail_admins(
        u'Новый коментарии',
        u'Новый коменатрии \n{0}\n{1}'.format(url, datetime.datetime.now()))
