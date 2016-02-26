# coding: utf-8

from django.conf.urls import url

from blog.views import blog_views, tags_view, posts_view

urlpatterns = [

    # ==========================================================================
    # АДМИНКА ТЕГОВ
    # ==========================================================================

    url(r'tags/delete/(?P<tag_id>\d+)', tags_view.tag_delete, name='tags_delete'),
    url(
        r'tags/edit/(?P<tag_id>\d+)',
        tags_view.TagsEditPage.as_view(),
        name='tags_edit'),
    url(
        r'tags',
        tags_view.TagsPage.as_view(),
        name='tags'),

    # ==========================================================================
    # АДМИНКА ПОСТОВ
    # ==========================================================================

    url(
        r'posts/edit/(?P<post_id>\d+)',
        posts_view.EditPostPage.as_view(),
        name='posts_edit'),
    url(
        r'posts/delete/(?P<post_id>\d+)',
        posts_view.delete_post,
        name='posts_delete'),

    # ==========================================================================
    url(
        r'comment_add/(?P<post_id>\d+)',
        blog_views.comment_add,
        name='comment_add'),
    url(
        r'post/(?P<post_id>\d+)',
        blog_views.PostPage.as_view(),
        name='post_page'),
    url(
        r'tag/(?P<tag_id>\d+)',
        blog_views.TagPage.as_view(),
        name='tags_page'),
    url(
        r'',
        blog_views.HomePage.as_view(),
        name='home_page'),
]
