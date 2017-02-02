# coding: utf-8

import datetime

from django.contrib.sitemaps import Sitemap
from django.core.urlresolvers import reverse

from application.constants import CONSPECTS_ALL


class ApplicationSitemap(Sitemap):

    changefreq = "weekly"
    priority = 0.5

    def items(self):
        today = datetime.date.today()
        lastmod = today - datetime.timedelta(weeks=5)
        return (
            {
                "url": "resume:home_page",
                "lastmod": lastmod,
            }, {
                "url": "conspects_page",
                "lastmod": lastmod,
            }
        )

    def lastmod(self, obj):
        return obj['lastmod']

    def location(self, obj):
        return reverse(obj["url"])


class ConspectsSitemap(Sitemap):

    changefreq = "monthly"
    priority = 0.5

    def items(self):
        today = datetime.date.today()
        lastmod = today - datetime.timedelta(weeks=5)
        return [
            {
                'location': conspect['url'],
                'lastmod': lastmod,
            } for conspect in CONSPECTS_ALL
        ]

    def lastmod(self, obj):
        """
        :param obj:
        :type obj: Post
        """
        return obj['lastmod']

    def location(self, obj):
        return obj['location']
