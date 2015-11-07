.. py:module:: pymongo.bulk

bulk - интерфейс для порционной записи данных
=============================================


BulkOperationBuilder
--------------------

.. py:class:: BulkOperationBuilder(collection, ordered=True)

    * `collection` - :py:class::`pymongo.collection.Collection`, коллекция для выполнения операции

    * `ordered` - выполнить все операции последовательно


    .. py:method:: execute(write_concern=None)

        Выполнить все операции


    .. py:method:: find(selector)

        Возвращает :py:class::`pymongo.bulk.BulkWriteOperation`, задает условие отбора для выполнения операции


    .. py:method:: insert(document)

        Добавляет документ


BulkUpsertOperation
-------------------

.. py:class:: BulkUpsertOperation(selector, bulk)
    
    Интерфейс для добалвения операции `upsert`


    .. py:method:: replace_one(replacement)

        Заменяет один документ, удовлетворяющий условию


    .. py:method:: update(update)

        Обновляет все документы, удовлетворяющий условию


    .. py:method:: update_one(update)

        Обновляет один документ, удовлетворяющий условию


BulkWriteOperation
------------------

.. py:class:: BulkWriteOperation(selector, bulk)

    Интерфейс для добалвения операции обновления и замены


    .. py:method:: remove()

        Удаляет все документы, удовлетворяющий условию


    .. py:method:: remove_one()

        Удаляет один документ, удовлетворяющий условию


    .. py:method:: replace_one(replacement)

        Заменяет одну запись, удовлетворяющий условию


    .. py:method:: update(update)

        Обновляет все документы, удовлетворяющий условию


    .. py:method:: update_one(update)

        Обновляет один документ, удовлетворяющий условию


    .. py:method:: upsert()

        Возвращает :py:class::`pymongo.bulk.BulkUpsetOperation`, указывает что все операции обновления должны быть upserts