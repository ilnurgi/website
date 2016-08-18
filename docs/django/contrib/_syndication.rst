Рассылки
========

.. code-block:: py

    # feeds.py

    from django.contrib.syndication.views import Feed
    from django.template.defaultfilters import truncatewords

    from .models import Post

    class LatestPostsFeed(Feed):
        title = 'My blog'
        link = '/blog/'
        description = 'New posts of my blog.'

        def items(self):
            return Post.published.all()[:5]

        def item_title(self, item):
            return item.title

        def item_description(self, item):
            return truncatewords(item.body, 30)

.. code-block:: py

    # urls.py

    from .feeds import LatestPostsFeed

    urlpatterns = [
        url(r'^feed/$', LatestPostsFeed(), name='post_feed'),
    ]

Feed
----

.. py:class:: django.contrib.syndication.views.Feed

    .. py:attribute:: author_name

        Автор канала

    .. py:attribute:: author_email

        Почта автора канала

    .. py:attribute:: author_link

        Адрес страницы об авторе канала

    .. py:attribute:: categories

        Список категории, к которым относятся данные канала

    .. py:attribute:: description

        Описание канала rss

    .. py:attribute:: feed_copyright

        Сведения о правах автора канала

    .. py:attribute:: item_author_email
    .. py:attribute:: item_author_link
    .. py:attribute:: item_author_name
    .. py:attribute:: item_categories
    .. py:attribute:: item_copyright
    .. py:attribute:: item_description
    .. py:attribute:: item_link
    .. py:attribute:: item_pubdate
    .. py:attribute:: item_title

    .. py:attribute:: link

        Адрес страницы, где выводятся данные, на основе которых генерируется канал

    .. py:attribute:: title

        Заголовок канала

    .. py:attribute:: ttl

        Время в секундах, в течение которого канал является актуальным

    .. py:attribute:: subtitle

        Описание канала atom

    .. py:method:: get_object(request)

        Возвращает объект

        Используется для филтрации новостей по конкретному объекту