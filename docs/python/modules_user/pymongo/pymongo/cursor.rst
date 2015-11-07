.. py:module:: pymongo.cursor

cursor - интсрумент для итерации по результатам запросов к БД
=============================================================


CursorType
----------

.. py:class:: CursorType

    Тип курсора


    .. py:attribute:: NON_TAILABLE

        стандартный курсор


    .. py:attribute:: TAILABLE

        курсор сохрянющий свою позицию

        Такое курсор не закрывается после получения послдених данных и могут вернуть новые данные с последней позиции


    .. py:attribute:: TAILABLE_AWAIT

        курсор сохраняющий свою позицию

        Курсор будет ждать в течении нескольких секунд после возвращения полного набора результата, поэтому он может вернуть доп добавленные данные в течении запроса


    .. py:attribute:: EXHAUST

        потоковый курсор

        БД будет возвращать данные клиенту, не дожидаясь от него результата чтения предыдущих данных


Cursor
------

.. py:class:: Cursor(**kwargs)

    Курсор

    Не должен создаваться через данный класс, а необходимо использовать курсор результата запросов

    * `collection` -

    * `filter=None` -

    * `projection=None` -

    * `skip=0` -

    * `limit=0` -

    * `no_cursor_timeout=False` -

    * `cursor_type=CursorType.NON_TAILABLE` -

    * `sort=None` -

    * `allow_partial_results=False` -

    * `oplog_replay=False` -

    * `modifiers=None` -

    * `manipulate=True` -

    >>> db.test.find()[50]
    >>> db.test.find()[20:50]


    .. py:attribute:: address

        Адрес БД

    
    .. py:attribute:: alive

        Может ли курсор вернуть ещё данные.

        Даже если и может, то вызов метода next() может возбудить исключение StopIteration

        Актуально для курсоров tailable курсоров


    .. py:attribute:: collection

        :py:class::`pymongo.collection.Collection` коллекция курсора


    .. py:attribute:: cursor_id

        Идентификатор курсора


    .. py:attribute:: retrivied

        Количесвто пуже полученных документов


    .. py:method:: add_option(mask)

        Установить флаг запроса, используя битовую маску

        >>> # tailable флаг
        >>> cursor.add_option(2)


    .. py:method:: batch_size(batch_size)
        
        Установить количесвто документов, возвращаемых курсором за раз.

        .. note::

            БД имеет ограниче на размер возвращаемой порции курсору, она будет приоритетнее чем количесвто записей в порции.

            Например если установить размер порции в 1,000,000 документов, вернется то количесвто документов, которое уместится в 4-16Мб.


    .. py:method:: clone()

        Возвращает новый курсор, копия текущего курсора


    .. py:method:: close()
        
        Закрывает/убивает курсор. Требуется только для PyPy, Jython и других питон интерпретаторов не использующих сборщик мусора.


    .. py:method:: comment(comment)

        Добаляет коментарии к курсору


    .. py:method:: count(with_limit_and_skip=False)
        
        Возвращает размер текущего запроса, количество документов

        * `with_limit_and_skip=False` - учитывать ограничения

        Возбуждает:

        * :py:class::`pymongo.errors.OperationFailure`


    .. py:method:: distinct(key)

        Возвращает список уникальных данных по ключю


    .. py:method:: explain()

        Возвращает план запроса курсора


    .. py:method:: hint(index)

        Добавляет "подсказку" для БД, какой индекс использовать

        >>> cur.hint([('field', ASCENDING)])
        >>> cur.hint('index_name')


    .. py:method:: limit(limit)

        Ограничивает количесвто возвращаемых данных курсором

        Возбуждает:

        * :py:class::`pymongo.errors.InvalidOperation`


    .. py:method:: max(spec)

        Добавляет оператор максимума, который определяет максимальную границу индекса


    .. py:method:: max_scan(max_scan)

        Огрничивает количесвто сканируемых документов

        Возбуждает:

        * :py:class::`pymongo.errors.InvalidOperation`


    .. py:method:: max_time_ms(max_time_ms)

        Задает время для выполнения запроса

        Возбуждает:

        * :py:class::`pymongo.errors.InvalidOperation`


    .. py:method:: min(spec)

        Добавляет оператор минимума, который определяет минимуальную границу индекса


    .. py:method:: next()

        Передвигает курсор на след позицию


    .. py:method:: remove_option(mask)

        Удаляет флаги запроса, используя битовую маску


    .. py:method:: rewind()

        Сбросить курсор


    .. py:method:: skip(skip)

        Пропустить первые указанные количесвто документов

        Возбуждает:

        * :py:class::`pymongo.errors.InvalidOperation`


    .. py:method:: sort(key_or_list, direction=None)
        
        Сортировка результата запроса

        Возбуждает:

        * :py:class::`pymongo.errors.InvalidOperation`

        >>> for doc in collection.find().sort('field', pymongo.ASCENDING):
        ...     print(doc)
        

        >>> for doc in collection.find().sort([
        ...         ('field1', pymongo.ASCENDING),
        ...         ('field2', pymongo.DESCENDING)]):
        ...     print(doc)

        >>> cursor = db.test.find(
        ...     {'$text': {'$search': 'some words'}},
        ...     {'score': {'$meta': 'textScore'}})
        >>> # Sort by 'score' field.
        >>> cursor.sort([('score', {'$meta': 'textScore'})])
        >>> for doc in cursor:
        ...     print(doc)


    .. py:method:: where(code)
        
        Добавляет условие в курсор

        * `code` - JS функция

        Возбуждает:

        * :py:class::`pymongo.errors.InvalidOperation`