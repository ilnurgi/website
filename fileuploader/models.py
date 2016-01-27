# coding: utf-8

import os

from django.contrib import admin
from django.db import models


class File(models.Model):
    file_name = models.CharField(max_length=100)
    file = models.FileField()
    created = models.DateTimeField(auto_now=True)

    def exists(self):
        return os.path.exists(self.file.path)

admin.site.register(File)
