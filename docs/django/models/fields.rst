Поля модели
===========

Field
-----

.. py:class:: django.db.models.Field(**kwargs)

    Базовый класс для полей модели

    * blank=False - булево, поле может хранить пустое значение

    * choices=None - список значений, которые может хранить поле

    * default=NOT_PROVIDED - значение поля по умолчанию

    * db_column=None - строка, имя поля таблицы, если не задано,
      будет использоваться имя поля модели

    * db_index=False - булево, создавать индекс для поля

    * editable=True - булево, пле редактируемо

    * help_text='' - строка, доп описание

    * max_length - число, максимальная длина поля

    * null=False - булево, поле может хранить значение null

    * primary_key=False - булево, поле является первичным ключом

    * unique=False - булево, значения в поле уникальны

    * unique_for_date=None - имя поля модели
      (:py:class:`DateTimeField` или :py:class:`DateField`)
      относительно которых данное поле уникально

    * unique_for_month=None - имя поля модели
      (:py:class:`DateTimeField` или :py:class:`DateField`)
      относительно которых данное поле уникально

    * unique_for_year=None - имя поля модели
      (:py:class:`DateTimeField` или :py:class:`DateField`)
      относительно которых данное поле уникально

    * verbose_name=None - имя поля

    * auto_created=False

    * error_messages=Non

    * db_tablespace=None

    * name=None

    * rel=None

    * serialize=True

    * validators=[]


AutoField
---------

.. py:class:: django.db.models.AutoField()

    Счетчик


BigIntegerField
---------------

.. py:class:: django.db.models.BigIntegerField()

    64-разрядное, длинное число.


BooleanField
------------

.. py:class:: django.db.models.BooleanField()

    Логическое поле

    .. code-block:: py

        is_done = models.BooleanField(
            default=False,
            db_index=True,
            verbose_name="done",
        )


CharField
---------

.. py:class:: django.db.models.CharField()

    Строковое поле

    Наследник :py:class:`Field`

    Обязательные поля:

    * max_length

    .. code-block:: py

        name = models.CharField(
            max_length=32,
            unique=True,
            verbose_name="name",
            unique_for_date="pubdate",
        )


DateField
---------

.. py:class:: django.db.models.DateField(**kwargs)

    Поле с датой

    Наследник :py:class:`Field`

    * auto_now=False - булево, автоматический прописывать текущее время
      при сохранении

    * auto_now_add=False - булево, автоматический прописывать текущее время
      при добавлении

    .. code-block:: py

        class Good(models.Model):

            updated = models.DateField(auto_now=True)


DateTimeField
-------------

.. py:class:: django.db.models.DateTimeField()

    Поле с датой и временем

    Наследник :py:class:`DateField`

    .. code-block:: py

        created = models.DateField(auto_now_add=True)
        updated = models.DateField(auto_now=True)


EmailField
----------

.. py:class:: django.db.models.EmailField(**kwargs)

    Поле с электронной почтой

    Наследник :py:class:`CharField`

    * max_length = 254

    .. code-block:: py

        email = models.EmailField()


FileField
---------

.. py:class:: django.db.models.FileField(**kwargs)

    Поле для хранения файла любого типа

    * upload_to - строка, путь к папке куда грузить файлы

    .. py:attribute:: name

        Путь к файлу, относитльно MEDIA_ROOT

    .. py:attribute:: size

        Размер файла в байтах

    .. py:attribute:: url

        Интернет адрес файла


FloatField
----------

.. py:class:: django.db.models.FloatField()

    Число с плавающей точкой


GenericIPAddressField
---------------------

.. py:class:: django.db.models.GenericIPAddressField()

    Поле с IPv4 или IPv6 адресом


ImageField
----------

.. py:class:: django.db.models.ImageField(**kwargs)

    Поле для хранения изображений

    Требует установленной библиоткеи pillow

    * upload_to - строка, путь к папке куда грузить файлы

    * width_field - имя поля модели, где будет храниться ширина изображения

    * height_field - имя поля модели, где будет храниться высота изображения

    .. code-block:: py

        image = models.ImageField(upload_to='images/')
        image = models.ImageField(upload_to='images/%Y/%m/%d')

    .. code-block:: py

        thumbnail_width = models.PositiveSmallIntegerField()
        thumbnail_height = models.PositiveSmallIntegerField()
        thumbnail = models.ImageField(
            upload_to='thumbnails/',
            width_field='thumbnail_width',
            height_field='thumbnail_height',
        )

    .. code-block:: py

        obj = SomeModel.objects.get()
        # obj.thumbnail.url

    .. py:attribute:: height

        Высота картинки

    .. py:attribute:: name

        Путь к файлу, относитльно MEDIA_ROOT

    .. py:attribute:: size

        Размер файла в байтах

    .. py:attribute:: url

        Интернет адрес файла

    .. py:attribute:: width

        Высота картинки

    .. py:method:: delete(save=True)

        Удаляет выбранный файл.

        Параметр save указывает, сохранять ли модель после удаления файла.

        .. code-block:: py

            class SomeModel(models.Model):

                def save(self, *args, **kwargs):
                    this_record = SomeModel.objects.get()
                    if this_record.thumbnail != self.thumbnail:
                        this_record.thumbnail.delete(save=False)
                    super().save(*args, **kwargs)

                def delete(self, *args, **kwargs):
                    self.thumbnail.delete(save=False)
                    super().delete(*args, **kwargs)




IntegerField
------------

.. py:class:: django.db.models.IntegerField()

    32-разрядное, обычное число

    .. code-block:: py

        from django.core.validators import (
            MinValueValidator,  MaxValueValidator)

        CATEGORIES = (
            (1, "car"),
            (2, "house"),
        )

        class Good(models.Model):

            category = models.IntegerField(
                choices=CATEGORIES,
                default=1,
                db_index=True,
            )

            discount = models.IntegerField(
                validators=[MinValueValidator(0),
                            MaxValueValidator(100)])


IPAddressField
--------------

.. py:class:: django.db.models.IPAddressField()

    Поле с IPv4 адресом


PositiveIntegerField
--------------------

.. py:class:: django.db.models.PositiveIntegerField()

    32-разрядное, положительное число


PositiveSmallIntegerField
-------------------------

.. py:class:: django.db.models.PositiveSmallIntegerField()

    16-разрядное положительное число


SlugField
---------

.. py:class:: django.db.models.SlugField(**kwargs)

    Короткий заголовок или название, которое включает только символы латиницы,
    цифры, дефисы и символы подчеркивания.

    Наследник :py:class:`CharField`

    * max_length = 50

    * db_index = True

    .. code-block:: py

        from django.utils.text import slugify

        class Image(models.Model):

            title = models.CharField(max_length=200)
            slug = models.SlugField(max_length=200, blank=True)

            def save(self, *args, **kwargs):
                self.slug = slugify(self.title)
                super(Image, self).save(*args, **kwargs)

SmallIntegerField
-----------------

.. py:class:: django.db.models.SmallIntegerField

    16-разрядное положительное число


TextField
---------

.. py:class:: django.db.models.TextField()

    Текстовое поле

    Наследник :py:class:`Field`

    .. code-block:: py

        description = models.TextField()


TimeField
---------

.. py:class:: django.db.models.TimeField()

    Поле со временем


URLField
--------

.. py:class:: django.db.models.URLField(**kwargs)

    Поле с интернет адресом

    Наследник :py:class:`CharField`

    * max_length = 200