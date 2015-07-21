.. py:method:: java.lang

Math - реализует ряд наиболее известных математических функций
==============================================================

Класс состоит из набора статических методов, производящих наиболее популярные математические вычисления и двух констант, имеющих особое значение в математике - это число Пи и экспонента. Часто этот класс еще называют классом-утилитой (Utility class).

Так как все методы класса статические нет необходимости создавать экземпляр этого класса - поэтому он и не имеет открытого конструктора. 

Нельзя так же и унаследовать этот класс, поскольку он объявлен с атрибутом final


.. py:class:: Math()

    
    .. py:attribute:: E

        `public static final double`

        Число e

    .. py:attribute:: PI

        `public static final double`

        Число Пи


.. py:method:: abs(double a) 
.. py:method:: abs(float a) 
.. py:method:: abs(int a) 
.. py:method:: abs(long a) 

    `static [double, float, int, long]`

    Возвращает абсолютное значение

    Вернет значения типа int, если в качестве параметра будут переданы значения типа byte, short, char.


.. py:method:: acos(double a) 

    `static double`

    Вернет значение арккосинуса угла в диапазоне от 0 до PI


.. py:method:: asin(double a) 

    `static double`

    Вернет значение арксинуса угла в диапазоне от -PI/2 до PI/2


.. py:method:: atan(double a) 

    `static double`

    Вернет значение арктангенса угла в диапазоне от -PI/2 до PI/2


.. py:method:: ceil(double a) 

    `static double`

    Возвращает наименьшее целое число которое больше a. 

    Угол задается в радианах


.. py:method:: floor(double a) 

    `static double`

    Возвращает целое число которое меньше a.

    Угол задается в радианах


.. py:method:: cos(double a) 

    `static double`

    Возвращает косинус угла (3)


.. py:method:: IEEEremainder(double a, double b) 

    `static double`

    Возвращает остаток от деления a/b по стандарту IEEE 754


.. py:method:: sin(double a) 

    `static double`

    Возвращает косинус угла


.. py:method:: tan(double a)

    `static double`

    Возвращает тангенс угла (3)


.. py:method:: exp(double a)

    `static double`

    Возвращает e в степени числа a


.. py:method:: log(double a)

    `static double`

    Возвращает натуральный логарифм числа a


.. py:method:: max(double a, double b) 
.. py:method:: max(float a, float b)
.. py:method:: max(long a, long b)
.. py:method:: max(int a, int b)

    `static [double, float, long, int]`

    Возвращает наибольшее из двух чисел


.. py:method:: min(double a, double b) 
.. py:method:: min(float a, float b) 
.. py:method:: min(long a, long b) 
.. py:method:: min(int a, int b) 

    `static [double, float, long, int]`

    Возвращает наименьшее из двух чисел типа int


.. py:method:: pow(double a, double b) 

    `static double`

    Возвращает а в степени b


.. py:method:: random() 

    `static double`

    Возвращает случайное число в диапазоне от 0.0 до 1.0


.. py:method:: rint(double a) 

    `static double`

    Возвращает int число, ближайшее к a


.. py:method:: round(double a) 

    `static long`

    Возвращает значение типа long ближайшее по значению к а


.. py:method:: sqrt(double a) 

    `static double`

    Возвращает положительный квадратный корень числа a


.. py:method:: toDegrees(double angrad) 

    `static double`

    Преобразует значение угла из радианов в градусы


.. py:method:: toRadians(double angdeg) 

    `static double`

    Преобразует значение угла из градусов в радианы