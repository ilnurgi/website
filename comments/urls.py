# coding: utf-8

from django.conf.urls import url

from comments import views

urlpatterns = [

    url(r'delete/(?P<comment_id>\d+)', views.comment_delete, name='delete'),
    url(
        r'edit/(?P<comment_id>\d+)',
        views.EditPage.as_view(),
        name='edit'),
    url(
        r'comments',
        views.HomePage.as_view(),
        name='home_page'),
]
