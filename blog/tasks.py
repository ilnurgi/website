# coding: utf-8

from celery.task import task

from django.core.mail import mail_admins


@task()
def send_email_notification(title, message):
    mail_admins(title, message)
