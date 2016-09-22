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
        results = []
        for doc_name in os.listdir(docs_path):
            doc_path = os.path.join(docs_path, doc_name)
            doc_build_path = os.path.join(docs_path, "_build")

            if os.path.exists(doc_build_path):
                os.removedirs(doc_build_path)

            if os.path.isdir(doc_path):
                executes.append(doc_name)
                results.append(u'\n\n'.join(subprocess.Popen(
                    ["make", "html"],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    cwd=doc_path).communicate()))

        send_email_notification.delay(
            title=u'Конспекты собраны',
            message=u'Конспекты собраны для:\n{0}\n\n{1}'.format(
                u'\n'.join(executes),
                u'\n\n\n'.join(results)))









