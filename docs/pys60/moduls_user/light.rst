.. py:module:: light

light
=====

Питоновский модуль для работы с подсветкой 

.. versionadded:: pys60 2.0.0

.. py:method:: disable_light_sensor()
    
    Выключает датчик света

.. py:method:: enable_light_sensor()
    
    Включает датчик света

.. py:method:: get() 
    
    Возвращает уровень подсветки смартфона

    >>> light.get()
    30

.. py:method:: is_light_sensor_enabled() 
    
    Возвращает статус датчика света.

    >>> light.is_light_sensor_enabled()
    0

.. py:method:: set(light) 
    
    Устанавливает уровень подсветки дисплея в значение light.
    
    >>> light.set(100)