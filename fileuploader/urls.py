# coding: utf-8

from django.conf.urls import url

from fileuploader import views

urlpatterns = [
    url(r'delete/(?P<file_id>\d+)', views.delete, name='delete'),
    url(
        r'',
        views.HomePage.as_view(),
        name='home_page'),
]
