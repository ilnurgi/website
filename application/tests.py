# coding: utf-8

import datetime

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import testcases

from application.constants import CONSPECTS, CONSPECTS_ALL
from blog.models import Post, Category


class ViewsTestCase(testcases.TestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(
            username="username",
            email="email@email.ru",
            password="password",
        )
        self.user.password_raw = "password"

    def test_home_page(self):

        response = self.client.get(reverse("resume:home_page"))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.template_name, ["resume.html"])
        self.assertIn('GOOGLE_SITE_VERIFICATIN', response.context_data)

    def test_sitemap(self):

        response = self.client.get(reverse("sitemap"))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.template_name, ["application/sitemap.html"])
        self.assertIn("categories", response.context_data)
        self.assertDictContainsSubset(
            {
                "conspects": CONSPECTS,
                "active_page": "sitemap",
            },
            response.context_data
        )

    def test_sitemap_with_data(self):

        category = Category.objects.create()
        Post.objects.create(
            published=True, category=category, title="123")

        response = self.client.get(reverse("sitemap"))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.template_name, ["application/sitemap.html"])
        self.assertDictContainsSubset(
            {
                "conspects": CONSPECTS,
                "active_page": "sitemap",
            },
            response.context_data
        )

        self.assertEqual(len(response.context_data["categories"]), 1)

    def test_sitemap_with_data_not_published(self):

        category = Category.objects.create()
        Post.objects.create(
            published=False, category=category, title="123")

        response = self.client.get(reverse("sitemap"))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.template_name, ["application/sitemap.html"])
        self.assertDictContainsSubset(
            {
                "conspects": CONSPECTS,
                "active_page": "sitemap",
            },
            response.context_data
        )

        self.assertEqual(len(response.context_data["categories"]), 0)

    def test_sitemap_with_data_not_published_superuser(self):

        self.client.post(
            reverse("login"),
            data={
                'username': self.user.username,
                'password': self.user.password_raw,
            })

        category = Category.objects.create()
        Post.objects.create(
            published=False, category=category, title="123")

        response = self.client.get(reverse("sitemap"))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.template_name, ["application/sitemap.html"])
        self.assertDictContainsSubset(
            {
                "conspects": CONSPECTS,
                "active_page": "sitemap",
            },
            response.context_data
        )

        self.assertEqual(len(response.context_data["categories"]), 1)

    def test_login_page(self):

        response = self.client.get(reverse("login"))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.template_name, "application/login.html")
        self.assertDictContainsSubset(
            {
                "conspects": CONSPECTS,
            },
            response.context_data
        )

    def test_login_logout(self):

        response = self.client.post(
            reverse("login"),
            data={
                'username': self.user.username,
                'password': self.user.password_raw,
            })

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("resume:home_page"))

        response = self.client.get(reverse("logout"))

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("resume:home_page"))

    def test_404(self):

        for url in (
            "/abracadabra",
            "/blog/abracadabra",
            "/blog/post/abracadabra",
            "/blog/post/525",
        ):

            response = self.client.get(url)
            self.assertEqual(response.status_code, 404)


class SiteMapXMLTestCase(testcases.TestCase):

    def setUp(self):

        today = datetime.date.today()
        lastmod = today - datetime.timedelta(weeks=5)
        self.urls = [
            {
                'lastmod': lastmod,
                'location': u'http://testserver/' + reverse("resume:home_page"),
            }, {
                'lastmod': lastmod,
                'location': u'http://testserver/' + reverse("conspects_page"),
            }]
        self.urls.extend(
            {
                'lastmod': lastmod,
                'location': u'http://testserver' + conspect['url'],
            } for conspect in CONSPECTS_ALL)

    def test_sitemap_xml(self):

        response = self.client.post(reverse("sitemap_xml"))
        self.assertIn("urlset", response.context_data)

        self.assertEqual(len(response.context_data["urlset"]), len(self.urls))
        for index, url in enumerate(response.context_data['urlset']):
            self.assertEqual(
                url['lastmod'],
                self.urls[index]['lastmod'],
                u"{}: {} != {}".format(
                    index, url['lastmod'], self.urls[index]['lastmod']))

    def test_sitemap_xml_post_not_published(self):

        category = Category.objects.create()
        Post.objects.create(category=category)
        self.test_sitemap_xml()

    def test_sitemap_xml_post_published(self):

        category = Category.objects.create(name="python")
        post = Post.objects.create(category=category, published=True, title="python")

        response = self.client.post(reverse("sitemap_xml"))
        self.assertIn("urlset", response.context_data)

        self.assertEqual(
            len(response.context_data["urlset"]),
            len(self.urls) + 1)
        self.assertDictContainsSubset(
            {
                "lastmod": post.modified,
                "location": (
                    u'http://testserver' + reverse(
                        "blog:post_detail",
                        args=[post.category.name, post.slug]))
            },
            response.context_data['urlset'][0]
        )
        for index, url in enumerate(response.context_data['urlset'][1:]):
            self.assertEqual(
                url['lastmod'],
                self.urls[index]['lastmod'],
                u"{}: {} != {}".format(
                    index, url['lastmod'], self.urls[index]['lastmod']))
