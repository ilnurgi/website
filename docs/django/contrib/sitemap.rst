Карта сайта
===========

.. code-block:: py

    # sitemaps.py

    from django.contrib.sitemaps import Sitemap
    from .models import Post

    class PostSitemap(Sitemap):
        changefreq = 'weekly'
        priority = 0.9

        def items(self):
            return Post.published.all()

        def lastmod(self, obj):
            return obj.publish


.. code-block:: py

    # urls.py

    from django.conf.urls import include, url
    from django.contrib.sitemaps.views import sitemap

    from blog.sitemaps import PostSitemap

    sitemaps = {
        'posts': PostSitemap,
    }

    urlpatterns = [
        url(
            r'^sitemap\.xml$',
            sitemap,
            {'sitemaps': sitemaps},
            name='django.contrib.sitemaps.views.sitemap',
        ),
    ]
