.. py:module:: dbm

dbm
===

Хранилище ключ - значение

.. code-block:: py

    import dbm

    db = dbm.open("dbm.db", "c")

    db["key1"] = "value1"

    db.close()

open()
======

.. py:method:: open(path, mode)

    Открывает и возвращает хранилище

    * mode - режим работы

        * r - чтение
        * w - запись
        * c - если файла нет, то создает и доступен для чтения и записи

