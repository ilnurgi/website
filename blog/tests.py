# coding: utf-8

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import testcases

from application.constants import CONSPECTS
from blog.models import Category, Post, Comment


class SuperUserTestCase(testcases.TestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(
            username="username",
            email="email@email.ru",
            password="password",
        )
        self.user.password_raw = "password"

        self.client.post(
            reverse("login"),
            data={
                'username': self.user.username,
                'password': self.user.password_raw,
            })

    def test_list(self):

        response = self.client.get(reverse("blog:list", args=[""]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.template_name, ["blog/post_list.html"])

        self.assertIn('view', response.context_data)

        self.assertIn('object_list', response.context_data)
        self.assertEqual(len(response.context_data['object_list']), 0)

        self.assertIn('categories', response.context_data)
        self.assertEqual(len(response.context_data['categories']), 0)

        self.assertDictContainsSubset(
            {
                "active_page": "blog",
                "conspects": CONSPECTS,
                "current_category": None,
            },
            response.context_data
        )

    def test_list_with_data(self):

        category = Category.objects.create(name="python")
        Post.objects.create(published=False, category=category, title="python")

        response = self.client.get(reverse("blog:list", args=[""]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.template_name, ["blog/post_list.html"])

        self.assertIn('view', response.context_data)

        self.assertIn('object_list', response.context_data)
        self.assertEqual(len(response.context_data['object_list']), 1)

        self.assertIn('categories', response.context_data)
        self.assertEqual(len(response.context_data['categories']), 1)

        self.assertDictContainsSubset(
            {
                "active_page": "blog",
                "conspects": CONSPECTS,
                "current_category": None,
            },
            response.context_data
        )

    def test_list_with_data2(self):

        category = Category.objects.create(name="python")
        Post.objects.create(
            published=True, category=category, title="python")

        response = self.client.get(reverse("blog:list", args=["python"]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.template_name, ["blog/post_list.html"])

        self.assertIn('view', response.context_data)

        self.assertIn('object_list', response.context_data)
        self.assertEqual(len(response.context_data['object_list']), 1)

        self.assertIn('categories', response.context_data)
        self.assertEqual(len(response.context_data['categories']), 1)

        self.assertDictContainsSubset(
            {
                "active_page": "blog",
                "conspects": CONSPECTS,
                "current_category": category,
            },
            response.context_data
        )

    def test_detail(self):

        category = Category.objects.create(name="python")
        post = Post.objects.create(
            published=False, category=category, title="python")

        Comment.objects.create(post=post, published=False)

        response = self.client.get(
            reverse("blog:post_detail", args=[post.category.name, post.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.template_name, ["blog/post_detail.html"])

        self.assertIn('view', response.context_data)

        self.assertIn('categories', response.context_data)
        self.assertEqual(len(response.context_data['categories']), 1)

        self.assertIn('object_comments', response.context_data)
        self.assertEqual(len(response.context_data['object_comments']), 1)

        self.assertDictContainsSubset(
            {
                "active_page": "blog",
                "conspects": CONSPECTS,
                "object": post,
            },
            response.context_data
        )

    def test_detail2(self):

        category = Category.objects.create(name="python")
        post = Post.objects.create(
            published=True, category=category, title="python")

        Comment.objects.create(post=post, published=True)

        response = self.client.get(
            reverse("blog:post_detail", args=[post.category.name, post.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.template_name, ["blog/post_detail.html"])

        self.assertIn('view', response.context_data)

        self.assertIn('categories', response.context_data)
        self.assertEqual(len(response.context_data['categories']), 1)

        self.assertIn('object_comments', response.context_data)
        self.assertEqual(len(response.context_data['object_comments']), 1)

        self.assertDictContainsSubset(
            {
                "active_page": "blog",
                "conspects": CONSPECTS,
                "object": post,
            },
            response.context_data
        )

    def test_create(self):

        response = self.client.get(reverse("blog:post_create"))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.template_name, ["blog/post_form.html"])

        self.assertIn('form', response.context_data)
        self.assertIn('view', response.context_data)

        self.assertDictContainsSubset(
            {
                "active_page": "blog",
                "conspects": CONSPECTS,
            },
            response.context_data
        )

    def test_create_error_category_not_exists(self):

        response = self.client.post(
            reverse("blog:post_create"),
            {
                "category": "1",
                "title": "python",
                "raw_content": "python",
                "published": "off",
            })

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.template_name, ["blog/post_form.html"])

        self.assertIn('form', response.context_data)
        self.assertIn('view', response.context_data)

        self.assertTrue(response.context_data["form"].errors)

        self.assertDictContainsSubset(
            {
                "active_page": "blog",
                "conspects": CONSPECTS,
            },
            response.context_data
        )
        self.assertEqual(Post.objects.count(), 0)

    def test_create3(self):

        category = Category.objects.create(name="python")

        response = self.client.post(
            reverse("blog:post_create"),
            {
                "category": category.id,
                "title": "python",
                "raw_content": "python",
                "published": "off",
            })

        self.assertEqual(response.status_code, 302)
        self.assertTrue(
            response.url.endswith(
                reverse("blog:post_detail", args=[category.name, "python"])))

        self.assertEqual(Post.objects.count(), 1)

    def test_update(self):

        # создаем запись
        category = Category.objects.create(name="python")

        response = self.client.post(
            reverse("blog:post_create"),
            {
                "category": category.id,
                "title": "python",
                "raw_content": "python",
                "published": False,
            })

        self.assertEqual(response.status_code, 302)
        self.assertTrue(
            response.url.endswith(
                reverse("blog:post_detail", args=[category.name, "python"])))

        post = Post.objects.get()
        self.assertEqual(Post.objects.count(), 1)
        self.assertEqual(post.category, category)
        self.assertEqual(post.title, "python")
        self.assertEqual(post.slug, "python")
        self.assertEqual(post.published, False)

        # а теперь обновляем

        response = self.client.post(
            reverse("blog:post_update", args=["python"]),
            {
                "category": category.id,
                "title": "python",
                "raw_content": "python",
                "published": True,
            })

        self.assertEqual(response.status_code, 302)
        self.assertTrue(
            response.url.endswith(
                reverse("blog:post_detail", args=[category.name, "python"])))

        post = Post.objects.get()
        self.assertEqual(Post.objects.count(), 1)
        self.assertEqual(post.category, category)
        self.assertEqual(post.title, "python")
        self.assertEqual(post.slug, "python")
        self.assertEqual(post.published, True)

    def test_delete(self):

        # создаем запись
        category = Category.objects.create(name="python")

        response = self.client.post(
            reverse("blog:post_create"),
            {
                "category": category.id,
                "title": "python",
                "raw_content": "python",
                "published": False,
            })

        self.assertEqual(response.status_code, 302)
        self.assertTrue(
            response.url.endswith(
                reverse("blog:post_detail", args=[category.name, "python"])))

        post = Post.objects.get()
        self.assertEqual(Post.objects.count(), 1)
        self.assertEqual(post.category, category)
        self.assertEqual(post.title, "python")
        self.assertEqual(post.slug, "python")
        self.assertEqual(post.published, False)

        # а теперь удаляем

        response = self.client.get(
            reverse("blog:post_delete", args=["python"]))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.template_name,
            [u'blog/post_confirm_delete.html'])

        response = self.client.post(
            reverse("blog:post_delete", args=["python"]))

        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.endswith(reverse("blog:list", args=[""])))

        self.assertEqual(Post.objects.count(), 0)

    def test_comment_create(self):

        # создаем запись
        category = Category.objects.create(name="python")
        post = Post.objects.create(category=category, title="python")

        response = self.client.post(
            reverse(
                "blog:comment_create", args=[post.slug]),
            {
                "content_raw": "some raw text"
            })

        self.assertEqual(response.status_code, 302)
        self.assertTrue(
            response.url.endswith(
                reverse(
                    "blog:post_detail", args=[post.category.name, post.slug])))

        comment = Comment.objects.get()
        self.assertEqual(Comment.objects.count(), 1)
        self.assertEqual(comment.user, self.user)
        self.assertEqual(comment.content_raw, "some raw text")
        self.assertNotEqual(comment.content, "")
        self.assertEqual(comment.published, False)

    def test_comment_create_not_content_raw(self):

        category = Category.objects.create(name="python")
        post = Post.objects.create(category=category, title="python")

        response = self.client.post(
            reverse(
                "blog:comment_create", args=[post.slug]),
            {
                "content_raw123": "some raw text"
            })

        self.assertEqual(response.status_code, 302)
        self.assertTrue(
            response.url.endswith(
                reverse(
                    "blog:post_detail", args=[post.category.name, post.slug])))

    def test_comment_create_post_not_exists(self):

        response = self.client.post(
            reverse("blog:comment_create", args=["python"]),
            {
                "content_raw": "some raw text"
            })

        self.assertEqual(response.status_code, 404)


class SimpleUserTestCase(testcases.TestCase):

    def test_list(self):

        response = self.client.get(reverse("blog:list", args=[""]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.template_name, ["blog/post_list.html"])

        self.assertIn('view', response.context_data)

        self.assertIn('object_list', response.context_data)
        self.assertEqual(len(response.context_data['object_list']), 0)

        self.assertIn('categories', response.context_data)
        self.assertEqual(len(response.context_data['categories']), 0)

        self.assertDictContainsSubset(
            {
                "active_page": "blog",
                "conspects": CONSPECTS,
                "current_category": None,
            },
            response.context_data
        )

    def test_list_with_data(self):

        category = Category.objects.create(name="python")
        Post.objects.create(published=False, category=category, title="python")

        response = self.client.get(reverse("blog:list", args=[""]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.template_name, ["blog/post_list.html"])

        self.assertIn('view', response.context_data)

        self.assertIn('object_list', response.context_data)
        self.assertEqual(len(response.context_data['object_list']), 0)

        self.assertIn('categories', response.context_data)
        self.assertEqual(len(response.context_data['categories']), 1)

        self.assertDictContainsSubset(
            {
                "active_page": "blog",
                "conspects": CONSPECTS,
                "current_category": None,
            },
            response.context_data
        )

    def test_list_with_data2(self):

        category = Category.objects.create(name="python")
        Post.objects.create(
            published=True, category=category, title="python")

        response = self.client.get(reverse("blog:list", args=["python"]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.template_name, ["blog/post_list.html"])

        self.assertIn('view', response.context_data)

        self.assertIn('object_list', response.context_data)
        self.assertEqual(len(response.context_data['object_list']), 1)

        self.assertIn('categories', response.context_data)
        self.assertEqual(len(response.context_data['categories']), 1)

        self.assertDictContainsSubset(
            {
                "active_page": "blog",
                "conspects": CONSPECTS,
                "current_category": category,
            },
            response.context_data
        )

    def test_detail(self):

        category = Category.objects.create(name="python")
        post = Post.objects.create(
            published=False, category=category, title="python")

        Comment.objects.create(post=post, published=False)

        response = self.client.get(
            reverse("blog:post_detail", args=[post.category.name, post.slug]))
        self.assertEqual(response.status_code, 403)

    def test_detail2(self):

        category = Category.objects.create(name="python")
        post = Post.objects.create(
            published=True, category=category, title="python")

        Comment.objects.create(post=post, published=True)

        response = self.client.get(
            reverse("blog:post_detail", args=[post.category.name, post.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.template_name, ["blog/post_detail.html"])

        self.assertIn('view', response.context_data)

        self.assertIn('categories', response.context_data)
        self.assertEqual(len(response.context_data['categories']), 1)

        self.assertIn('object_comments', response.context_data)
        self.assertEqual(len(response.context_data['object_comments']), 1)

        self.assertDictContainsSubset(
            {
                "active_page": "blog",
                "conspects": CONSPECTS,
                "object": post,
            },
            response.context_data
        )

    def test_create(self):

        response = self.client.get(reverse("blog:post_create"))

        self.assertEqual(response.status_code, 403)

    def test_create_error_category_not_exists(self):

        response = self.client.post(
            reverse("blog:post_create"),
            {
                "category": "1",
                "title": "python",
                "raw_content": "python",
                "published": "off",
            })

        self.assertEqual(response.status_code, 403)

    def test_update(self):

        # создаем запись
        category = Category.objects.create(name="python")
        Post.objects.create(
            published=True, category=category, title="python")

        # а теперь обновляем

        response = self.client.post(
            reverse("blog:post_update", args=["python"]),
            {
                "category": category.id,
                "title": "python",
                "raw_content": "python",
                "published": True,
            })

        self.assertEqual(response.status_code, 403)

    def test_delete(self):

        # создаем запись
        category = Category.objects.create(name="python")
        Post.objects.create(
            published=True, category=category, title="python")

        # а теперь удаляем

        response = self.client.get(
            reverse("blog:post_delete", args=["python"]))

        self.assertEqual(response.status_code, 403)

    def test_comment_create(self):

        # создаем запись
        category = Category.objects.create(name="python")
        post = Post.objects.create(
            category=category, title="python", published=True)

        response = self.client.post(
            reverse("blog:comment_create", args=["python"]),
            {
                "content_raw": "some raw text",
                "user_name": "some user name",
                "user_email": "some user email",
            })

        self.assertEqual(response.status_code, 302)
        self.assertTrue(
            response.url.endswith(
                reverse(
                    "blog:post_detail", args=[post.category.name, post.slug])))

        comment = Comment.objects.get()
        self.assertEqual(Comment.objects.count(), 1)
        self.assertEqual(comment.user, None)
        self.assertEqual(comment.user_name, "some user name")
        self.assertEqual(comment.content_raw, "some raw text")
        self.assertNotEqual(comment.content, "")
        self.assertEqual(comment.published, False)

    def test_comment_create_403(self):

        # создаем запись
        category = Category.objects.create(name="python")
        Post.objects.create(category=category, title="python")

        response = self.client.post(
            reverse("blog:comment_create", args=["python"]),
            {
                "content_raw": "some raw text",
                "user_name": "some user name",
                "user_email": "some user email",
            })

        self.assertEqual(response.status_code, 403)

    def test_comment_create_not_content_raw(self):

        category = Category.objects.create(name="python")
        post = Post.objects.create(category=category, title="python")

        response = self.client.post(
            reverse("blog:comment_create", args=["python"]),
            {
                "content_raw123": "some raw text"
            })

        self.assertEqual(response.status_code, 302)
        self.assertTrue(
            response.url.endswith(
                reverse(
                    "blog:post_detail", args=[post.category.name, post.slug])))

    def test_comment_create_post_not_exists(self):

        response = self.client.post(
            reverse("blog:comment_create", args=["python"]),
            {
                "content_raw": "some raw text"
            })

        self.assertEqual(response.status_code, 404)
