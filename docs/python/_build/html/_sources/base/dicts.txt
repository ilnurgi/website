dict - Словари
==============

>>> {'1': 1}
{'1': 1}
>>> dict('1'=1)
{'1': 1}
>>> d1, d2 = { "а": 1, "Ь": 2 }, { "а": 3, "с": 4, "d": 5 )
>>> 
>>> d1.keys() - d2. keys ()
{ 'Ь'}
»> d2.keys() - d1. keys ()
{'с',
'd'}
»> d1.keys() & d2. keys ()

.. py:class:: dict

    словарь


    .. py:method:: clear()
        
        Очищает словарь
        
        >>> d = {'first': 'pervi', 'second': 'vtoroi'}
        >>> d.clear()
        >>> d
        {}


    .. py:method:: copy()
        
        Возвращает словарь, копию
        
        >>> d = {'first': 'pervi', 'second': 'vtoroi'}
        >>> d.copy()
        {'second': 'vtoroi', 'first': 'pervi'}


    .. py:method:: fromkeys(<Последовательность> [ , <Значение по умолчанию>=None])

        Создает новый словарь, ключами которого являются элементы последовательности с дефолтным значением.

        >>> d = dict.fromkeys('abc')
        >>> d
        {'a': None, 'b': None, 'c', None}


    .. py:method:: get(<Ключ> [, <Значение по умолчанию>=None])
        
        Возвращает значение словаря по ключу

        >>> d = {'first': 'pervi', 'second': 'vtoroi'}
        >>> d.get('fif', 'fifa net')
        'fifa net'


    .. py:method:: has_key(key)
        
        True | False, имеет ли словарь ключ

        >>> d = {'first': 'pervi', 'second': 'vtoroi'}
        >>> d.has_key('first')
        True
        >>> d.has_key('firsttttt')
        False

        .. warning:: 

            Вместо has_key рекомендуется использовать in

            >>> d = {'first': 'pervi', 'second': 'vtoroi'}
            >>> 'first' in d
            True
            >>> 'firsttttt' in d
            False

    .. py:method:: items()
        
        Возвращает список кортежей (ключ, значение) элементов словаря.

        .. versionchanged:: 3.x

            возвращает объект :py:class::`dict_items`
        
        >>> d = {'first': 'pervi', 'second': 'vtoroi'}
        >>> d.items()
        [('second', 'vtoroi'), ('first', 'pervi')]

    .. py:method:: iterkeys()
        
    .. py:method:: itervalues()

    .. py:method:: iteritems()

    .. py:method:: keys()
        
        Возвращает список, ключи словаря

        .. versionchanged:: 3.x

            возвращает объект :py:class:`dict_keys`

            >>> d1, d2 = {"а": 1, "b": 2}, {"а": 3, "с": 4, "d": 5}
            >>> d1.keys() | d2.keys() # объединение 
            {'a', 'c', 'b', 'd'}
            >>> d1.keys() - d2.keys() # разница
            {'b'}
            >>> d2.keys() | d1.keys() # разница
            {'c', 'd'}
            >>> d1.keys() & d2.keys() # одинаковые ключи
            {'a'}
            >>> d1.keys() ^ d2.keys() # уникальные ключи
            {'c', 'b', 'd'}
        
        >>> d = {'first': 'pervi', 'second': 'vtoroi'}
        >>> d.keys()
        ['second', 'first']


    .. py:method:: pop(key[, default])

        Возвращает значение по ключу, удалив запись из словаря.

        * Если ключа нет, возвращается указанное дефолтное значение.
        * Если ключа нет и не указано дефолтное значение, возбуждается исключение `KeyError`


    .. py:method:: popitem()

        Возвращает случайную пару (ключ, значение) из словаря, удаляя его из словаря.


    .. py:method:: setdefault(key[, default=None])    
        
        Возвращает значение по ключу, если такого ключа нет, то возвращается дефолтное значение, при этом добавив в словарь новую запись.
        
        >>> dict = {1 : 'One', 2 : 'Two', 3 : 'Three'}
        >>> setdefault(4, 'Four')
        'Four'
        >>> dict
        {1 : 'One', 2 : 'Two', 3 : 'Three', 4: 'Four'}


    .. py:method:: update(key=value)
    .. py:method:: update(dict)
    .. py:method:: update([(key, value)])
    .. py:method:: update(((key, value), ))
        
        Обновляет словарь.

        >>> d = {"а": 1, "b": 2}
        >>> d.update(c=З, d=4)
        >>> d
        {'а': 1, 'с': 3, 'b': 2, 'd': 4}
        >>> d.update({"c": 10, "d": ·20))
        >>> d
        {'а': 1, 'с': 10, 'Ь': 2, 'd': 20}
        >>> d.update([("d", 80), ("е", 6)])
        >>> d
        {'а': 1; 'с': 10, 'Ь': 2, 'е': б, 'd': 80}


    .. py:method:: values()
        
        Возвращает список значений словаря

        .. versionchanged:: 3.x

            возвращает объект :py:class:`dict_values`
        
        >>> d = {'first': 'pervi', 'second': 'vtoroi'}
        >>> d.values()
        ['vtoroi', 'pervi']


.. py:class:: dict_items

    ключи и значения словаря в виде кортежей, который может быть получен с помощью метода словаря items.

    .. versionadded:: 3.x


.. py:class:: dict_keys

    ключи словаря, который может быть получен с помощью метода словаря keys.

    .. versionadded:: 3.x


.. py:class:: dict_values

    значения словаря, который может быть получен с помощью метода словаря values.

    .. versionadded:: 3.x


Генераторы словаря
------------------

>>> {key:value for key, value in ((1,1), (2,2))}
{1: 1, 2: 2}


Особенности работы со словарем
------------------------------

.. glossary::
    
    Ситуация. Добавить в словарь ключ, и в качестве значения должен быть список, если ключ уже есть, то добавить значение в список.

        Вариант 1.

        >>> dict_ = {}
        >>> key = 3
        >>> value = 3
        >>> if key in dict_:
                dict_[key].append(value) 
            else:
                dict_[key] = [value]
        >>> dict_
        {3: [3]}

        Вариант 2. Рекомендуемый мной.

        >>> dict_ = {}
        >>> key = 3
        >>> value = 3
        >>> dict_.setdefault(key, []).append(value)
        >>> dict_
        {3: [3]}

        Во втором варианте, всю логику из Варианта 1 выполняет сам интерпретатор. Что оптимальней и быстрее.