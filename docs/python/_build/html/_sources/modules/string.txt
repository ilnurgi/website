.. py:module:: string

string
======

Модуль для работы со строками 

.. py:method:: atoi(s[, base]) 
    
    :param base: система исчисления, дефолт десятичная

    Возвращает число, преобразованное из аргумента.
    
    >>> string.atoi('1')
    1

.. py:method:: atol(s[, base]) 

    :param base: система исчисления, дефолт десятичная

    Возвращает число типа long, преобразованное из аргумента.
    
    >>> string.atol('1')
    1L

.. py:method:: atof(s) 
    
    Возвращает число типа float, преобразованное из аргумента.
    
    >>> string.atof('1')
    1.0

.. py:method:: split(s[, sep=' ' [, maxsplit]]) 

    Возвращает список, полученный разделением строки s, разделителем sep. Если аргумент sep не указан, его значением по умолчанию является пробел.
    
    >>> string.split('ilnur privet kak dela')
    ['ilnur', 'privet', 'kak', 'dela']

.. py:method:: join(words[, sep=' ']) 
    
    Возвращает строку, объединяет все слова списка в одну строку символов, при этом слова отделяются друг от друга символом, указанным в sep.
    
    string.join(['ilnur', 'privet', 'kak', 'dela'])
    'ilnur privet kak dela'

.. py:method:: find(s, sub[, start[, end] } ) 
    
    Возвращает число, позицию вхождения искомой строки sub в строке s.