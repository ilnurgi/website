# coding: utf-8

from django.contrib.sitemaps import Sitemap

from .models import Post


class BlogSitemap(Sitemap):

    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Post.objects.filter(published=True)

    def lastmod(self, obj):
        """
        :param obj:
        :type obj: Post
        """
        return obj.modified

    def location(self, obj):
        """
        :param obj:
        :type obj: Post
        """
        return obj.get_absolute_url()
