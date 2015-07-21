.. py:module:: fractions

fractions
=========

.. py:class:: Fraction([numerator=0 [, denominator=1]])
.. py:class:: Fraction(fraction)
.. py:class:: Fraction(s)

    Рациональное число. Экземпляр f класса Fraction поддерживает все обычные математические операции.

    :param int numerator: числитель
    :param int denominator: знаменатель
    :param fraction: экземпляр numbers.Rational
    :param str s: строкове представление значения, "3/7", "4.5"

    >>> fractions.Fraction(3,4)
    Fraction(3, 4)
    >>> fractions.Fraction(“1.75”)
    Fraction(7, 4)

    .. py::method:: from_float(f)

        Создает дробь, представляющую точное значение аргумента. Метод класса.

        :param float f: значение

        >>> fractions.Fraction.from_float(3.1415926)
        Fraction(3537118815677477, 1125899906842624)

    .. py:method:: from_decimal(d)

        Создает дробь, представляющую точное значение аргумента. Метод класса.

        :param Decimal d: значение

    .. py:attribute:: numerator

        Числитель

    .. py:attribute:: denominator 

        Знаменатель

    .. py:method:: limit_denominator([max_denominator=1000000])

        Возвращает дробь, ближайшую к экземпляыру. 

        :param int max_denominator: наибольший возможный числитель

.. py:method:: gcd(a, b)

    Вычисляет наибольший общий делитель целых чисел a и b. Результат имеет тот же знак, что и число b, если оно не равно нулю; и знак числа a – в противном случае.