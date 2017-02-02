Связи моделей
=============

ForeignObject
-------------

.. py:class:: django.db.models.ForeignObject(**kwargs)

    Базовый класс для свзяей таблиц

    * to - ссылка на модель таблицы

    * on_delete=CASCADE - что делатьс записью, при удалении первичной записи

        * CASCADE - удалить записи вторичной таблицы

        * PROTECT - не удалять и вызывать исключение

        * SET_NULL - записать значение NULL

        * SET_DEFAULT - записать дефолтное значение для поля


ForeignKey
----------

.. py:class:: django.db.models.ForeignKey(**kwargs)

    Связь один ко многим

    Наследник :py:class:`ForeignObject`

    .. code-block:: py

        class Category(models.Model):

            name = models.CharField(...)

        class Good(models.Model):

            category = models.ForeignKey(
                Category,
                on_delete=models.SET_NULL,
                related_name='goods',
            )


ManyToManyField
---------------

.. py:class:: django.db.models.ManyToManyField()

    Связь многие ко многим

    .. code-block:: py

        users_like = models.ManyToManyField(
            settings.AUTH_USER_MODEL,
            related_name='images_liked',
            blank=True)


OneToOneField
-------------

.. py:class:: django.db.models.OneToOneField(**kwargs)

    Связь один к одному

    Наследник :py:class:`ForeignKey`

    .. code-block:: py

        class Category(models.Model):

            name = models.CharField(...)

        class Good(models.Model):

            category = models.OneToOneField(
                Category,
            )