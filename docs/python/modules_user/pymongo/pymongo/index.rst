.. py:module:: pymongo

pymongo - драйвер для MongoDB
=============================

.. py:attribute:: version

    Строка, текущая версия модуля


.. py:attribute:: MongoClient

    Ссылка на :py:class:`pymongo.mongo_client.MongoClient`


.. py:attribute:: pymongo.MongoReplicaSetClient

    Ссылка на :py:class:`pymongo.mongo_replica_set_client.MongoReplicaSetClient`


.. py:attribute:: pymongo.ReadPreference

    Ссылка на :py:class:`pymongo.read_preferences.ReadPreference`


.. py:method:: pymongo.has_c()

    Возвращает булео, рсширение нписано на С.


.. py:attribute:: pymongo.MIN_SUPPORTED_WIRE_VERSION

    Минималная версия протокола поддержки


.. py:attribute:: pymongo.MAX_SUPPORTED_WIRE_VERSION

    Максимальная версия протокола поддержки


Константы профилировщика
------------------------

.. py:attribute:: OFF

    Профилировщик выключен


.. py:attribute:: SLOW_ONLY

    Профилировка медленных запросов


.. py:attribute:: ALL

    Профилировка всех запросов


Объекты модуля
--------------

.. toctree::
   :maxdepth: 1

   auth
   bulk
   collection
   command_cursor
   cursor
   cursor_manager
   database
   errors
   message
   mongo_client
   operations
   pool
   read_preferences
   results
   son_manipulator
   uri_parser
   write_concern
