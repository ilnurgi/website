# coding: utf-8

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import testcases

from application.constants import CONSPECTS
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
