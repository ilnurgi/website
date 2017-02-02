bytearray
=========

.. py:class:: bytearray([source[, encoding[, errors='replace']]])

    * source - источник (:py:class:`str`, :py:class:`list`,  :py:class:`tuple`)
    * encoding -  кодировка для :py:class:`str`
    * errors -  обработка ошибок для :py:class:`str`
        * `strict` - при ошибке возбуждается исключение :py:class:`UnicodeDecodeError`
        * `replace` - неизвестный символ заменяется символом, имеющим код \uFFFD
        * `ignore` - неизвестные символы игнорируются

    изменяемая последовательность байтов.

    Тип `bytearray` аналогичен типу :py:class:`bytes`,
    но позволяет изменять элементы по индексу и содержит дополнительные методы,
    позволяющие добавлять и удалять элементы.

    .. code-block:: py

        type(bytearray("Строка", "utf-8"))
        # <class 'bytearray'>

        s = bytearray("str", "cpl251")
        s[O] = 49
        s
        # bytearray(b'ltr')
        s.append(55)
        s
        # bytearray(b'ltr7')

        bytearray("cтpoкa" 1 "ср1251")
        # bytearray(b'\xf1\xf2\xf0\xee\xea\xe0')

        b= bytearray([2251 2261 2241 1741 1701 160])
        b
        # bytearray (b '\xe1\xe2\xe0\xae\xaa\xa0' )

        str(b, "ср866")
        # 'строка'


    .. py:method:: append(bytes)

        добавляет элемент в конец объекта

        .. code-block:: py

            b = bytearray('string', 'ascii')
            b.append(b'1')
            b
            # bytearray(b'string1')

            b + b'2'
            # bytearray(b'string12')

            b += b'2'
            b
            # bytearray(b'string12')


    .. py:method:: decode([encoding='utf-8'][, errors='strict'])

        возвращает строку


    .. py:method:: extend(bytes)

        добавляет последовательность элементов в конец объекта

        .. code-block:: py

            b = bytearray('string', 'ascii')
            b.extend(b'123')
            b
            # bytearray(b'string123')

            b + b'45'
            # bytearray(b'string12345')

            b += b'45'
            # bytearray(b'string1234')


    .. py:method:: insert(index, int)

        добавяет элемент по позиции

        .. code-block:: py

            b = bytearray('string', 'ascii')
            b.insert(0, b'1')
            b
            # bytearray(b'1string')


    .. py:method:: pop([index])

        удаляет элемент из массива и возвращает его

        .. code-block:: py

            b = bytearray('string', 'ascii')
            b.pop()
            # 103

            b
            # bytearray(b'strin')

            del b[0]
            # bytearray(b'trin')


    .. py:method:: remove(int)

        удаляет первый элемент, содержащий указанное значение

        .. code-block:: py

            b = bytearray('string', 'ascii')
            b.remove(b's')
            # bytearray(b'tring')


    .. py:method:: reverse()

        изменяет порядок следования элементов на противоположный

        .. code-block:: py

            b = bytearray('string', 'ascii')
            b.reverse()
            b
            # bytearray(b'gnirts')