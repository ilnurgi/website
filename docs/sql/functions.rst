Вспомогательные функции
=======================

.. _function_aggregate: Агрегатные функции

Агрегатные функции
------------------


.. py:method:: AVG(<поле>)  

    среднее значение в указанном поле

    .. code-block:: c

        SELECT AVG(age) from table


.. py:method:: COUNT(<поле> | *)
    
    количество записей в указанном поле

    .. code-block:: c

        SELECT COUNT(*) from table


.. py:method:: MAX(<поле>)  

    максимальное значение в указанном поле

    .. code-block:: c

        SELECT MAX(age) from table


.. py:method:: MIN(<поле>)
    
    минимальное значение в указанном поле

    .. code-block:: c

        SELECT MIN(age) from table


.. py:method:: SUM(<поле>)   

    сумма значение в указанном поле

    .. code-block:: c

        SELECT SUM(age) from table

