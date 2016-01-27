# coding: utf-8

from django.conf.urls import url

from fileuploader import views

urlpatterns = [
    url(
        r'',
        views.HomePage.as_view(),
        name='home_page'),
]
