Метаданные
==========

.. code-block:: py

    class Good(models.Model):

        class Meta:

            db_table = 'db_table'
            ordering = ['id', '-date']
            unique_together = ['name', 'date']
            verbose_name = ''
            verbose_name_plural = ''


db_table
--------

Строка, имя таблицы. По умолчанию - имяПриложения_имяТаблицы


ordering
--------

Список полей, сортировка по умолчанию


unique_together
---------------

Список полей, значения которых должны быть уникальны


verbose_name
------------

Строка, название модели


verbose_name_plural
-------------------

Строка, название модели во множественном числе