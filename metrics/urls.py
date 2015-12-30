# coding: utf-8

from django.conf.urls import url

from metrics import views

urlpatterns = [
    url(
        r'cpu_data',
        views.metrics_cpu_data,
        name='metrics_cpu_data'),
    url(
        r'cpu_hour_data',
        views.metrics_cpu_hour_data,
        name='metrics_cpu_hour_data'),
    url(
        r'mem_data',
        views.metrics_mem_data,
        name='metrics_mem_data'),
    url(
        r'mem_hour_data',
        views.metrics_mem_hour_data,
        name='metrics_mem_hour_data'),
    url(
        r'system',
        views.MetricsSystem.as_view(),
        name='metrics_system'),
    url(
        r'',
        views.MetricsHomePage.as_view(),
        name='metrics_home_page'),
]
