frozenset
=========

.. py:class:: frozenset()

    не изменяемые множества

    .. code-block:: py

        frozenset('str')
        # frozenset({'s', 't', 'r'})

    .. py:method:: copy()

        Возвращает копию объекта


    .. py:method:: difference(set)

        Возвращает множество, разницу между множествами

        .. code-block:: py

            {1,2,3} - {1,2,4}
            # {3}

            {1,2,3}.difference(set([1,2,4]))
            # {3}


    .. py:method:: intersection(set)

        Возвращает пересечение множеств, элементы которые существуют в обоих множествах

        .. code-block:: py

            {1,2,3}.intersection({1,2,4})
            # {1,2}

            set([1,2,3]) & set([1,2,4])
            # {1,2}


    .. py:method:: isdisjoint(set)

        Возвращает :py:class:`bool`, множества не имеют одинаковых элементов

        .. code-block:: py

            {1,2,3}.isdisjoint({4,5,6})
            # True

            {1,2,3}.isdisjoint({4,5,1})
            # False


    .. py:method:: issubset(set)

        Возвращает булево, входит ли исходное множество в указанное

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

        Проверяет, входит ли указанное множество в исходное множество

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


    .. py:method:: symmetric_difference(set)

        Возвращает множество, которое не содержит одинаковых элементов

        .. code-block:: py

            s = {1,2,3}
            s.symmetric_difference(set([1,2,4]))
            # {3, 4}

            {1,2,3}  ^ {1,2,4}
            # {3, 4}

    .. py:method:: union(set)

        Возвращает новое множество, объединенное из двух.

        .. code-block:: py

            s = {1, 2, 3}
            s.union(set([4, 5, 6]))
            # {1, 2, 3, 4, 5, 6}

            s | set([4,5,6])
            # {1, 2, 3, 4, 5, 6}
