# coding: utf-8

from django.conf.urls import url

from metrics import views

urlpatterns = [
    url(
        r'cpu_data',
        views.cpu_data,
        name='cpu_data'),
    url(
        r'cpu_hour_data',
        views.cpu_hour_data,
        name='cpu_hour_data'),
    url(
        r'mem_data',
        views.mem_data,
        name='mem_data'),
    url(
        r'mem_hour_data',
        views.mem_hour_data,
        name='mem_hour_data'),
    url(
        r'system',
        views.System.as_view(),
        name='system'),
    url(
        r'',
        views.HomePage.as_view(),
        name='home_page'),
]
