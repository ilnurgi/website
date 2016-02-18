# coding: utf-8

from celery.task import task

from django.core.mail import mail_admins


@task()
def send_email_notification():
    mail_admins('123', '123123123123123')
