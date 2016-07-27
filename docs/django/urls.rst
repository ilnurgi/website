Роутинг
=======

.. code-block:: py

    # urls.py

    from django.conf import settings
    from django.conf.urls import patterns, include, url, static
    from django.contrib import admin

    from application import views

    urlpatterns = patterns('',
        url(r'^admin/', url(admin.site.urls)),
        url(r'^application/', url("application.urls")),
        url(r'^application/index', views.index, name="index"),
        url(r'^good/(?P<good_id>\d+)', views.good, name="good"),
        url(r'^good/(?P<good_id>\d+)', views.IndexView.as_view(), name="good"),
        url(r'^good/', include('blog.urls', namespace="blog", app_name="blog"),
    )

    if settings.DEBUG:
        urlpatterns += static.static(
            settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

