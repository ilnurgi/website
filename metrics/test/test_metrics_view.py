# coding: utf-8

from django.conf import settings
from django.core.management import call_command
from django.test import TestCase


class TestParsingNginxAccess(TestCase):

    def setUp(self):
        pass