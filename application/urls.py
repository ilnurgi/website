"""ilnurgi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from application import views as app_view
from blog import urls as blog_urls
from fileuploader import urls as fileuploader_urls
from metrics import urls as metric_urls

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include(blog_urls, namespace='blog')),
    url(
        r'^fileuploader/',
        include(fileuploader_urls, namespace='fileuploader')),
    url(r'^login/', app_view.Login.as_view(), name='login'),
    url(r'^logout/', app_view.Logout.as_view(), name='logout'),
    url(r'^metrics/', include(metric_urls, namespace='metrics')),
    url(r'^$', app_view.HomePage.as_view(), name='home_page'),
]

if settings.DEBUG:
    urlpatterns.extend(
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
