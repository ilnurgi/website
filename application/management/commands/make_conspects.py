# coding: utf-8

import os
import subprocess

from django.conf import settings
from django.core.management.base import BaseCommand

from blog.tasks import send_email_notification


class Command(BaseCommand):
    """
    собираем инофрмацию по загруженности сервера
    """

    def handle(self, *args, **options):

        docs_path = os.path.join(settings.BASE_DIR, 'docs')
        executes = []
        for doc_name in os.listdir(docs_path):
            doc_path = os.path.join(docs_path, doc_name)
            if os.path.isdir(doc_path):
                executes.append(doc_name)
                proc = subprocess.Popen(
                    ["make", "html"],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    cwd=doc_path)

        send_email_notification.delay(
            title=u'Конспекты собраны',
            message=u'Конспекты собраны для:\n{}'.format(u'\n'.join(executes)))









