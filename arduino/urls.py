# coding: utf-8

from django.conf.urls import url

from arduino import views

urlpatterns = [
    url(
        r'',
        views.view,
        name='arduino_view')
]
