.. py:module:: locale

locale 
======

>>> import locale
>>> # Для кодировки windows-1251
>>> loca1e.setlocale(locale.LC_ALL, "Russian Russia.l251")
'Russian Russia .1251'
>>> # Устанавливаем локаль по умолчанию
>>> locale.setlocale(locale.LC_ALL, "")
'Russian Russia .1251'
>>> # Получаем текущее значение
>>> lоса1е.getlocale()
('Russian_Russia', '1251')
>>> # Получаем текущее значение категории locale.LC COLLATE
>>> locale.getlocale(locale.LC_COLLATE)
('Russian _ Russia', '1251')

Методы модуля
-------------

.. py:method:: getlocale([category])

    возвращает текущее значение локали


.. py:method:: localeconv()

    возвращает словарь с настройками локали

    >>> locale.localeconv()
    {
        'mon_decirnal_point': ', ', 
        'int_frac_digits': 2, 
        'p_sep_by_space': О,
        ...
    }

.. py:method:: setlocale(category [, locale])

    :param category: категория локали
    
    настройка совокупности локали системы


Категории локали
----------------

.. py:attribute:: LC_ALL

    значение локали для всех режимов

.. py:attribute:: LC_COLLIATE

    значение локали для сравнения строк

.. py:attribute:: LC_CTYPE

    значение локали для перевода символов в нижний или верхний регистр

.. py:attribute:: LC_MONETARY

    значение локали для отображения денежных едениц

.. py:attribute:: LC_NUMERIC

    значение локали для форматирования чисел

.. py:attribute:: LC_TIME

    значение локали для форматирования даты и времени

