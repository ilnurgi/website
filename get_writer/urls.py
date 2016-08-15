# coding: utf-8

from django.conf.urls import url

from .views import get_writer

urlpatterns = [
    url(r'', get_writer, name="home")
]
