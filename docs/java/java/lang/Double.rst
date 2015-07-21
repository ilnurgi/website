.. py:module:: java.lang

Double - класс обертка над double
=================================


.. py:class:: Double()
.. py:class:: Double(String str)

    Наследник :py:class::`java.lang.Number`

    Реализует интерфейс :py:class::`java.lang.Comparable`
    
    .. py:staticmethod:: doubleToLongBits(Double double)

        возвращает двоичное предстваление объекта


    .. py:staticmethod:: isNan(Double double)

        возвращает булево, значение объекта не число


    .. py:staticmethod:: isInfinite(Double double)

        возвращает булево, значение объекта бесконечность


    .. py:staticmethod:: parseDouble(String str)

        возвращает Double из переданной строки


    .. py:staticmethod:: valueOf(Double double)

        возвращает число с точкой


    .. py:attribute:: NAN

        константа не числа


    .. py:attribute:: NEGATIVE_INFINITY

        константа отрицательной бесконечности


    .. py:attribute:: MAX_VALUE

        константа максимального значения


    .. py:attribute:: MIN_VALUE

        константа минимального значения значения


    .. py:attribute:: POSITIVE_INFINITY

        константа положительной бесконечности
