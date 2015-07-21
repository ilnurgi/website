.. py:module:: indicators

indicators
==========

Модуль для изменения значений в статусной строке 

.. py:method:: set_battery(set) 
    
    :param set: уровень
    
    Устанавливает уровень заряда

    >>> indicators.set_battery(1)

.. py:method:: set_gprs_icon(set)

    :param set: режим
    
    Устанавливает режим работы смартфона

    >>> indicators.set_gprs_icon(1)

.. py:method:: set_gprs(set)

    :param set: режим

    Устанавливает режим работы смартфона

    >>> indicators.set_gprs(1)
    
.. py:method:: set_signal(set) 
    
    :param set: уровень

    Устанавливает уровень сигнала
    
    >>> indicators.set_signal(1)

.. py:method:: start_charging() 
    
    Включает индикатор зарядки
    
    >>> indicators.start_charging()

.. py:method:: stop_charging() 
    
    Выключает индикатор зарядки 
    
    >>> indicators.stop_charging()