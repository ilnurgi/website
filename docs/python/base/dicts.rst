dict
====

dict
----

.. py:class:: dict()

    Словарь

    .. code-block:: py

        {'1': 1}
        dict(name=1)

        d1, d2 = {"а": 1, "b": 2}, {"а": 3, "с": 4, "d": 5}
        d1.keys() | d2.keys()
        # объединение, {'a', 'c', 'b', 'd'}

        d1.keys() - d2.keys()
        # разница, {'b'}

        d2.keys() | d1.keys()
        # разница, {'c', 'd'}

        d1.keys() & d2.keys()
        # одинаковые ключи, {'a'}

        d1.keys() ^ d2.keys()
        # уникальные ключи, {'c', 'b', 'd'}


    .. py:method:: clear()
        
        Очищает словарь

        .. code-block:: py
        
            d = {'first': 'pervi', 'second': 'vtoroi'}
            d.clear()
            # d = {}


    .. py:method:: copy()
        
        Возвращает словарь, копию

        .. code-block:: py

            d = {'first': 'pervi', 'second': 'vtoroi'}
            d.copy()
            # {'second': 'vtoroi', 'first': 'pervi'}


    .. py:method:: fromkeys(iter_object [ , default_value=None])

        Возвращает :py:class:`dict`,
        ключами которого являются элементы последовательности с дефолтным значением.

        .. code-block:: py

            dict.fromkeys('abc')
            # {'a': None, 'b': None, 'c', None}


    .. py:method:: get(key [, default_value=None])
        
        Возвращает значение словаря по ключу

        .. code-block:: py

            d = {'first': 'pervi', 'second': 'vtoroi'}
            d.get('fif', 'fifa net')
            # 'fifa net'


    .. py:method:: has_key(key)
        
        Возвразает :py:class:`bool`, имеет ли словарь ключ

        .. code-block:: py

            d = {'first': 'pervi', 'second': 'vtoroi'}
            d.has_key('first')
            # True

            d.has_key('firsttttt')
            # False

        .. warning:: 

            Вместо has_key рекомендуется использовать in

            .. code-block:: py

                d = {'first': 'pervi', 'second': 'vtoroi'}
                'first' in d
                # True

                'firsttttt' in d
                # False


    .. py:method:: items()
        
        Возвращает список кортежей (ключ, значение) элементов словаря.

        .. versionchanged:: 3.x

            возвращает объект :py:class:`dict_items`

        .. code-block:: py

            d = {'first': 'pervi', 'second': 'vtoroi'}
            d.items()
            # [('second', 'vtoroi'), ('first', 'pervi')]

    .. py:method:: iterkeys()
        
    .. py:method:: itervalues()

    .. py:method:: iteritems()

    .. py:method:: keys()
        
        Возвращает список, ключи словаря

        .. versionchanged:: 3.x

            возвращает объект :py:class:`dict_keys`

        .. code-block:: py

            d = {'first': 'pervi', 'second': 'vtoroi'}
            d.keys()
            # ['second', 'first']


    .. py:method:: pop(key[, default])

        Возвращает значение по ключу, удалив запись из словаря.

        * Если ключа нет, возвращается указанное дефолтное значение.

        * Если ключа нет и не указано дефолтное значение, возбуждается исключение `KeyError`


    .. py:method:: popitem()

        Возвращает случайную пару (ключ, значение) из словаря, удаляя его из словаря.

        .. code-block:: py

            {'first': 'pervi', 'second': 'vtoroi'}.popitem()
            # ('first', 'pervi')


    .. py:method:: setdefault(key[, default=None])    
        
        Возвращает значение по ключу, если такого ключа нет, то возвращается дефолтное значение, при этом добавив в словарь новую запись.

        .. code-block:: py

            d = {1 : 'One', 2 : 'Two', 3 : 'Three'}
            d.setdefault(4, 'Four')
            # 'Four'

            d
            # {1 : 'One', 2 : 'Two', 3 : 'Three', 4: 'Four'}


    .. py:method:: update(key=value)
    .. py:method:: update(dict)
    .. py:method:: update([(key, value)])
    .. py:method:: update(((key, value), ))
        
        Обновляет словарь.

        .. code-block:: py

            d = {"а": 1, "b": 2}
            d.update(c=3, d=4)
            # d = {'а': 1, 'с': 3, 'b': 2, 'd': 4}

            d.update({"c": 10, "d": 20))
            # d = {'а': 1, 'с': 10, 'Ь': 2, 'd': 20}

            d.update([("d", 80), ("е", 6)])
            # d = {'а': 1; 'с': 10, 'Ь': 2, 'е': б, 'd': 80}


    .. py:method:: values()
        
        Возвращает список значений словаря

        .. versionchanged:: 3.x

            возвращает объект :py:class:`dict_values`

        .. code-block:: py

            d = {'first': 'pervi', 'second': 'vtoroi'}
            d.values()
            # ['vtoroi', 'pervi']


dict_items
----------

.. py:class:: dict_items

    Ключи и значения словаря в виде кортежей,
    который может быть получен с помощью метода словаря items.

    .. versionadded:: 3.x


dict_keys
---------

.. py:class:: dict_keys

    Ключи словаря, который может быть получен с помощью метода словаря keys.

    .. versionadded:: 3.x


dict_values
-----------

.. py:class:: dict_values

    Значения словаря, который может быть получен с помощью метода словаря values.

    .. versionadded:: 3.x


Генераторы словаря
------------------

.. code-block:: py

    {key:value for key, value in ((1,1), (2,2))}
    # {1: 1, 2: 2}


Особенности работы со словарем
------------------------------

.. glossary::
    
    Добавить в словарь ключ, и в качестве значения должен быть список,
    если ключ уже есть, то добавить значение в список.

        .. code-block:: py

            d = {}
            key = 3
            value = 3
            if key in d:
                d[key].append(value)
            else:
                d[key] = [value]
            # d = {3: [3]}

        .. code-block:: py

            d = {}
            key = 3
            value = 3
            d.setdefault(key, []).append(value)
            # d = {3: [3]}

        Во втором варианте, всю логику из Варианта 1 выполняет сам интерпретатор.

        Что оптимальней и быстрее.