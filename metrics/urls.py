# coding: utf-8

from django.conf.urls import url

from metrics import views

urlpatterns = [
    url(
        r'cpu',
        views.MetricsCpu.as_view(),
        name='metrics_cpu'),

    url(
        r'',
        views.MetricsHomePage.as_view(),
        name='metrics_home_page'),
]
