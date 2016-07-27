Модель
------

.. code-block:: py

    from django.db import models

.. py:class:: Model()

    Базовый класс модели

    По умолчанию имеет единственно поле - id.

    .. py:method:: get_absolute_url()

        Возвращает абсолютный путь до объекта

        .. code-block:: py

            from django.core.urlresolvers import reverse

            class Post(models.Model):

                def get_absolute_url(self):
                    return reverse('blog:post_detail', args=[])

    .. py:method:: delete()

        Удаялет модель

        .. code-block:: py

            class Good(models.Model):

                def delete(self, *args, **kwargs):
                    super(Good, self).delete(*args, **kwargs)


    .. py:method:: save()

        Сохраняет модель

        .. code-block:: py

            class Good(models.Model):

                def save(self, *args, **kwargs):
                    super(Good, self).save(*args, **kwargs)

.. toctree::
    :maxdepth: 1

    meta
    fields
    relations
    query
    migrations