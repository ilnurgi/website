# coding: utf-8

from django.conf.urls import url

from blog import views

urlpatterns = [
    url(
        r'',
        views.BlogHomePage.as_view(),
        name='blog_home_page'),
]
