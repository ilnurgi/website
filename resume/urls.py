# coding: utf-8

from django.conf.urls import url

from resume import views

urlpatterns = [
    url(
        r'',
        views.HomePage.as_view(),
        name='home_page'),
]
