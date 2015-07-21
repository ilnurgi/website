.. py:module:: profiles

profiles
========

Модуль для работы с режимами смартфона.

.. versionadded:: pys60 2.0

.. py:method:: get_ap()
    
    Возвращает номер активного режима.
    
    >>> profiles.get_ap()
    1

.. py:method:: profiles()
    
    Возвращает список кортежей режимов
    
    >>> profiles.profiles()
    [(0, u'General'), (1, u'Silent'), (2, u'Meeting'), (3, u'Outdoor'), (4, u'Pager'), (5, u'Offline')]

.. py:method:: set_ap(ap)
    
    Устанавливает режим смартфона
    
    >>> profiles.set_ap(0)