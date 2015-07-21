.. py:module:: java.lang

Character - класс обертка над char
==================================

.. py:class:: Character(char c)

    Реализует интерфейс :py:class::`java.lang.Comparable`


    .. py:method:: charValue()

        Возвращает значение

        public char


    .. py:staticmethod:: digit(char ch, ib radix)

        переводит цифру ch системы счисления с основанием radix в ее числовое значение типа int


    .. py:staticmethod:: forDigit(int digit, int radix)

        выполняет обратное преобразование целого числа digit в соответствующую цифру (тип char ) в системе счисления с основанием radix


    .. py:staticmethod:: getName(int code)


    .. py:method:: isDefined()

        выясняет, определен ли символ в кодировке Unicode
    

    .. py:method:: isDigit(char c) 

        `public static boolean`

        Является ли цифрой

    
    .. py:method:: isLetter(char c)

        `public static boolean`

        Является ли буквой


    .. py:method:: isLetterOrDigit(char c)

        `public static boolean`

        Является ли цифрой или буквой


    .. py:method:: isIdentifierIgnorable() 

        выясняет, нельзя ли использовать символ в идентификаторах


    .. py:method:: isIdentifierStart(char c) 

        `public static boolean`

        Является ли символ подходящим для того, чтобы с него начиналось наименование переменной JAVA


    .. py:method:: isISOControl() 

        определяет, является ли символ управляющим


    .. py:method:: isBmpCodePoint()

        определяет, лежит ли код символа в диапазоне \u0000–\uFFFF


    .. py:method:: isSupplementaryCodePoint()

        определяет, что код символа больше \uFFFF;
    

    .. py:method:: isJavaIdentifierPart() 

        выясняет, можно ли использовать символ в идентификаторах
    

    .. py:method:: isJavaIdentifierStart() 

        определяет, может ли символ начинать идентификатор


    .. py:method:: isLowerCase()

        определяет, записан ли символ в нижнем регистре


    .. py:method:: isSpaceChar()

        выясняет, является ли символ пробелом в смысле Unicode


    .. py:method:: isTitleCase()

        проверяет, является ли символ титульным


    .. py:method:: isUnicodeIdentifierPart()

        выясняет, можно ли использовать символ в именах Unicode


    .. py:method:: isUnicodeIdentifierStart()

        проверяет, является ли символ буквой Unicode


    .. py:method:: isUpperCase()

        проверяет, записан ли символ в верхнем регистре


    .. py:method:: isWhitespace()

        выясняет, является ли символ пробельным


    .. py:method:: toString()

        строковое представление объекта


    .. py:method:: toLowerCase()
    .. py:method:: toUpperCase()
    .. py:method:: toTitleCase()


    .. py:attribute:: MAX_RADIX


    .. py:attribute:: MIN_RADIX