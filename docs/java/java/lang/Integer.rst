.. py:module:: java.lang

Integer - класс обертка над int
===============================


.. py:class:: Integer()    
.. py:class:: Integer(String s)

    throws NumberFormatException

.. py:class:: Integer(int i)

    Наследник :py:class::`java.lang.Number`

    Реализует интерфейс :py:class::`java.lang.Comparable`


    .. py:method:: compareTo(Integer int)

        возвращает результат сравнения объектов


    .. py:method:: intValue()

        возвращает значение объекта

        public int


    .. py:staticmethod:: parseInt(String str)

        Преобразует строку в число, представляющую десятичную запись целого числа

        public static int throws NumberFormatException


    .. py:staticmethod:: parseInt(String str, int radx)

        Преобразует строку в число, представляющую запись целого числа в системе счисления radix

        public static int throws NumberFormatException


    .. py:staticmethod:: toBinaryString(Integer int)

        Двоичное представление

        pubic static String


    .. py:staticmethod:: toHexString(Integer int)

        Шестнадцатеричное представление

        pubic static String


    .. py:staticmethod:: toOctalString(Integer int)

        Восьмеричное представление

        pubic static String


    .. py:staticmethod:: valueOf(String s)

        возвращает объект из числа

        public static Integer


    .. py:staticmethod:: valueOf(String s, int radix)

        возвращает объект из числа

        public static Integer


    .. py:attribute:: MAX_VALUE

        константа максимального значения


    .. py:attribute:: MIN_VALUE

        константа минимального значения