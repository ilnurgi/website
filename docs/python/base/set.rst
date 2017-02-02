set
===

.. py:class:: set()

    Множества используются для хранения неупорядоченных коллекций уникальных объектов.

    Множество может содержать только элементы неизменяемых типов,
    например числа, строки, кортежи.

    .. code-block:: py

        set([1,1,1,1,2])
        set(1, 2)
        set('abc')
        set('a', 'b', 'c')
        {1,2,3}
        set(1,2,3)

    .. py:method:: add(obj)

        Добавляет новый объект в множество


    .. py:method:: clear()

        Очищает множество


    .. py:method:: copy()

        Возвращает копию объекта


    .. py:method:: difference(set)

        Возвращает :py:class:`set`, разницу между множествами

        .. code-block:: py

            {1,2,3} - {1,2,4}
            # {3}
            {1,2,3}.difference(set([1,2,4]))
            # {3}


    .. py:method:: difference_update(set)

        Удаляет элементы множества, которые присутствуют в обоих множествах

        .. code-block:: py

            s = {1,2,3}
            s.difference_update(set([1,2,4]))
            # s = {3}

            s -= set([3,4,5])
            # s = {}


    .. py:method:: discard(obj)

        Удаляет объект из множества.


    .. py:method:: intersection(set)

        Возвращает множество :py:class:`set`, элементы которого существуют в обоих множествах

        .. code-block:: py

            {1,2,3}.intersection({1,2,4})
            # {1,2}

            set([1,2,3]) & set([1,2,4])
            # {1,2}


    .. py:method:: intersection_update(set)

        В исходном множестве останутся только множества, которые есть в обоих множествах

        .. code-block:: py

            s = {1,2,3}
            s.intersection_update(set([1,2,4]))
            # s = {1,2}

            s &= {1,6,7}
            # s = {1}


    .. py:method:: isdisjoint(set)

        Возвращает :py:class:`bool`, множества не имеют одинаковых элементов

        .. code-block:: py

            {1,2,3}.isdisjoint({4,5,6})
            # True

            {1,2,3}.isdisjoint({4,5,1})
            # False


    .. py:method:: issubset(set)

        Возвращает :py:class:`bool`, входит ли исходное множество в указанное

        .. code-block:: py

            s = {1,2,3}
            s.issubset(set([1,2,3,4]))
            # True

            {1,2,3} <= {1,2,3}
            # True

            {1,2,3} <= {1,2,3,4}
            # True

            {1,2,3} < {1,2,3}
            # False

            {1,2,3} < {1,2,3,4}
            # True


    .. py:method:: issuperset(set)

        Возвращает :py:class:`bool`, входит ли указанное множество в исходное множество

        .. code-block:: py

            s = {1,2,3}
            s.issuperset(set([1,2]))
            # True

            {1,2,3} >= {1,2}
            # True

            {1,2,3} >= {1,2,3}
            # True

            {1,2,3} > {1,2}
            # True

            {1,2,3} > {1,2,3}
            # False


    .. py:method:: pop()

        Возвращает произвольный объект множества, удалив его из множества


    .. py:method:: remove(obj)

        Удаляет объект из множества


    .. py:method:: symmetric_difference(set)

        Возвращает множество :py:class:`set`, которое не содержит одинаковых элементов

        .. code-block:: py

            s = {1,2,3}
            s.symmetric_difference(set([1,2,4]))
            # {3, 4}

            {1,2,3}  ^ {1,2,4}
            # {3, 4}


    .. py:method:: symmetric_difference_update(set)

        Оставляет в исходном множестве все элементы, кроме одинаковых

        .. code-block:: py

            s = {1,2,3}
            s.symmetric_difference_update(set([1,2,4]))
            # s = {3, 4}

            {1,2,3} ^= {1,2,4}
            # {3, 4}


    .. py:method:: union(set)

        Возвращает новое множество :py:class:`set`, объединенное из двух.

        .. code-block:: py

            s = {1, 2, 3}
            s.union(set([4, 5, 6]))
            # s = {1, 2, 3, 4, 5, 6}

            s | set([4, 5, 6])
            # s= {1, 2, 3, 4, 5, 6}


    .. py:method:: update(set)

        Добавляет в множество новое множество

        .. code-block:: py

            s = {1,2,3}
            s.update(set([4,5,6]))
            # s = {1, 2, 3, 4, 5, 6}

            s |= {7, 8, 9}
            # s = {1, 2, 3, 4, 5, 6, 7, 8, 9}

    .. py:method:: remove(obj)



Генератор множеств
------------------

.. versionadded:: 3.x

.. code-block:: py

    { i for i in [1,2,3,1]}
    # {1,2,3}