# coding: utf-8

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.http.response import HttpResponse

from application import views as app_view
from application.constants import CONSPECTS
from application.sitemap import ApplicationSitemap, ConspectsSitemap

from blog import urls as blog_urls
from blog.sitemaps import BlogSitemap
from cars import urls as cars_urls
from fileuploader import urls as fileuploader_urls
from metrics import urls as metric_urls
from resume import urls as resume_urls


urlpatterns = [
    url(
        r'^sitemap\.xml$',
        "django.contrib.sitemaps.views.sitemap",
        {
            "sitemaps": {
                "main": ApplicationSitemap,
                "blog": BlogSitemap,
                "conspects": ConspectsSitemap,
            }
        },
        "sitemap_xml"),
    url(
        r'^robots\.txt$',
        lambda r: HttpResponse(
            "User-Agent: *\nDisallow: \nHost: ilnurgi1.ru\n",
            content_type="text/plain")),
    url(
        r'^admin/',
        include(admin.site.urls)),
    url(
        r'^blog/',
        include(blog_urls, namespace='blog')),
    url(
        r'^fileuploader/',
        include(fileuploader_urls, namespace='fileuploader')),
    url(
        r'^sitemap/',
        app_view.SiteMap.as_view(), name='sitemap'),
    url(
        r'^metrics/',
        include(metric_urls, namespace='metrics')),
    url(
        r'^conspects/$',
        app_view.ConspectsPage.as_view(),
        name='conspects_page'),
    url(
        r'^cars/',
        include(cars_urls, namespace='cars')),
    url(
        r'^login/',
        "django.contrib.auth.views.login",
        {
            "template_name": "application/login.html",
            "extra_context": {
                "conspects": CONSPECTS,
            }
        },
        'login'),
    url(
        r'^logout/',
        "django.contrib.auth.views.logout",
        {
            "next_page": "resume:home_page"
        },
        'logout'),
    url(
        r'^$',
        include(resume_urls, namespace="resume")),
]

if settings.DEBUG:
    urlpatterns.extend(
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
