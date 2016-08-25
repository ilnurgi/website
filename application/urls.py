# coding: utf-8

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from application import views as app_view
from application.constants import CONSPECTS
from blog import urls as blog_urls
from fileuploader import urls as fileuploader_urls
from metrics import urls as metric_urls
from resume import urls as resume_urls


urlpatterns = [
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
