# coding: utf-8

from django.conf.urls import url

from metrics import views as metrics_views

urlpatterns = [
    url(
        r'last_month_visiters',
        metrics_views.LastMonthVisiters.as_view(),
        name='metrics_last_month_visiters'),

    url(
        r'',
        metrics_views.MetricsHomePage.as_view(),
        name='metrics_home_page'),
]
