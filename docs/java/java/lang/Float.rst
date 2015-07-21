.. py:module:: java.lang

Float - класс обертка над float
===============================


.. py:class:: Float()

    Наследник :py:class::`java.lang.Number`

    Реализует интерфейс :py:class::`java.lang.Comparable`
    
    .. py:staticmethod:: floatToIntBits()()

        возвращает двоичное представление числа


    .. py:staticmethod:: isNan()

        возвращает булево, число не число


    .. py:staticmethod:: isInfinite()

        возвращает булево, число бесконечность


    .. py:staticmethod:: parseFloat(String str)

        возвращает число с плавающей точкой из строки


    .. py:attribute:: MAX_VALUE

        константа максимального значения


    .. py:attribute:: MIN_VALUE

        константа минимального значения значения


    .. py:attribute:: NAN

        константа не числа


    .. py:attribute:: NEGATIVE_INFINITY

        константа отрицательной бесконечности


    .. py:attribute:: POSITIVE_INFINITY

        константа положительной бесконечности