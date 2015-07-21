.. py:module:: lang

lang
====

.. versionadded:: pys60 2.0

Модуль для работы с языком смартфона

.. py:method:: get_input_language() 
    
    Возвращает номер языка активного на ввод.
    
    >>> lang.get_input_language()
    1

.. py:method:: get_phone_language() 
    
    Возвращает номер языка смартфона.
    
    >>> lang.get_phone_language()
    16

.. py:method:: get_predicative_input() 
    
    Возвращает статус Т9.
    
    >>> lang.get_predicative_input()
    0

.. py:method:: set_input_language(lang) 
    
    Устанавливает номер языка активного на ввод.
    
    >>> lang.set_input_language(16)

.. py:method:: set_phone_language(lang) 
    
    Устанавливает номер языка смартфона.
    
    >>> lang.set_phone_language(1)

.. py:method:: set_predicative_input(status) 
    
    Устанавливает статус Т9.
    
    >>> lang.set_predicative_input(1)