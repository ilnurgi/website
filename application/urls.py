# coding: utf-8

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from application import views as app_view
from blog import urls as blog_urls
from comments import urls as comments_urls
from fileuploader import urls as fileuploader_urls
from metrics import urls as metric_urls
from get_writer import urls as get_writer_urls

urlpatterns = [
    url(r'^get_writer/', include(get_writer_urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include(blog_urls, namespace='blog')),
    url(
        r'^fileuploader/',
        include(fileuploader_urls, namespace='fileuploader')),
    url(r'^login/', app_view.Login.as_view(), name='login'),
    url(r'^sitemap/', app_view.SiteMap.as_view(), name='sitemap'),
    url(r'^logout/', app_view.Logout.as_view(), name='logout'),
    url(r'^metrics/', include(metric_urls, namespace='metrics')),
    url(r'^comments/', include(comments_urls, namespace='comments')),
    url(
        r'^conspects/$',
        app_view.ConspectsPage.as_view(),
        name='conspects_page'),
    url(r'^$', app_view.HomePage.as_view(), name='home_page'),
]

if settings.DEBUG:
    urlpatterns.extend(
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
