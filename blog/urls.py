# coding: utf-8

from django.conf.urls import url

from blog import views

urlpatterns = [

    url(
        r'comment_create/(?P<post_slug>.+)',
        views.comment_create,
        name='comment_create'),
    url(
        r'post/create',
        views.PostCreateView.as_view(),
        name='post_create'),
    url(
        r'post/edit/(?P<slug>.+)',
        views.PostUpdateView.as_view(),
        name='post_update'),
    url(
        r'post/delete/(?P<slug>.+)',
        views.PostDeleteView.as_view(),
        name='post_delete'),
    url(
        r'post/(?P<slug>.+)',
        views.PostDetailView.as_view(),
        name='post_detail'),
    url(
        r'(?P<category_name>\w*)$',
        views.PostListView.as_view(),
        name='list'),
]
