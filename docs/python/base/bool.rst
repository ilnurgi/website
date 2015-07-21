bool - логический тип данных
============================

.. py:class:: bool

    логический тиn данных. Может содержать значения True или False, которые ведут себя как числа 1 и о соответственно

    >>> type(True), type(False)
    (<class 'bool'>, <class 'bool'>)
    >>> int(True), int(False)
    (1, 0)


Функции для работы с :py:class:`bool`
-------------------------------------


.. py:function:: bool(obj)

    возвращает :py:class:`bool`, преобразованный объект в логический тип данных

    >>> bool(0), bool(1), bool(''), bool('cnhjrf')
    False, True, False, True
