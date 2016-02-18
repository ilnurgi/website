# coding: utf-8

from celery.task import task

from django.core.mail import mail_admins


@task()
def send_email_notification():
    mail_admins(u'Новый коментарии', u'Новый коменатрии')
