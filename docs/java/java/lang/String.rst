.. py:module:: java.lang

String - представляет средства работы с символьными строками
============================================================


::

    String abc = "abc"; 
    Strings = new String("immutable");


.. py:class:: String()

    Наследник :py:class::`java.lang.Object`

    .. py:method:: String()

        создается объект с пустой строкой


    .. py:method:: String(String str)

        конструктор копирования: из одного объекта создается его точная копия, поэтому данный конструктор используется редко


    .. py:method:: String(StringBuffer str)

        преобразованная копия объекта класса StringBuffer


    .. py:method:: String(StringBuilder str)

        преобразованная копия объекта класса StringBuilder


    .. py:method:: String(byte[] byteArray)

        объект создается из массива байтов byteArray


    .. py:method:: String(char[] charArray)

        объект создается из массива charArray символов Unicode


    .. py:method:: String(byte[] byteArray, int offset, int count)

        объект создается из части массива байтов byteArray , начинающейся с индекса offset и содержащей count байтов


    .. py:method:: String(char[] charArray, int offset, int count)

        то же, но массив состоит из символов Unicode

    
    .. py:method:: String(int[] intArray, int offset, int count)

        то же, но массив состоит из символов Unicode, записанных в массив целого типа, что позволяет использовать символы Unicode, занимающие больше двух байтов


    .. py:method:: String(byte[] byteArray, String encoding)

        символы, записанные в массиве байтов, задаются в Unicode-строке с учетом кодировки encoding


    .. py:method:: String(byte[] byteArray, int offset, int count, String encoding)

        то же самое, но только для части массива


    .. py:method:: String(byte[] byteArray, Charset charset)

        символы, записанные в массиве байтов, задаются в Unicode-строке с учетом кодировки, заданной объектом charset


    .. py:method:: String(byte[] byteArray, int offset, int count, Charset charset)

        то же самое, но только для части массива


    .. py:staticmethod:: copyValueOf(char[] charArray)
    .. py:staticmethod:: copyValueOf(char[] charArray, int offset, int length)
    .. py:staticmethod:: isEmpty()
    .. py:staticmethod:: getChars(int begin, int end, char[] dst, int ind)
    .. py:staticmethod:: substring(int begin, int end)
    .. py:staticmethod:: substring(int begin)
    .. py:staticmethod:: split(str str)
    .. py:staticmethod:: equals(Object obj)
    .. py:staticmethod:: equalsIgnoreCase(Object obj)
    .. py:staticmethod:: compareTo(String str)
    .. py:staticmethod:: compareToIgnoreCase(String str)
    .. py:staticmethod:: indexOf(int ch)

        возвращает число, позицию, указанного символа. поиск начинается сначала


    .. py:staticmethod:: indexOf(String sub)

        возвращает число, позицию, указанной строки. поиск начинается сначала


    .. py:staticmethod:: indexOf(int ch, int ind)

        возвращает число, позицию, указанного символа. поиск ведется от указанной позиции


    .. py:staticmethod:: lastIndexOf(int ch)

        возвращает число, позицию, указанного символа. поиск начинается сконца


    .. py:staticmethod:: lastIndexOf(int ch, int ind)

        возвращает число, позицию, указанного символа. поиск начинается сконца с указанной позиции


    .. py:staticmethod:: startsWith(String sub)

        возвращает булево, начинается ли строка от указанной строки


    .. py:staticmethod:: startsWith(String sub, int ind)

        возвращает булево, начинается ли строка от указанной строки с указанной позиции


    .. py:staticmethod:: endsWith(String sub)

        возвращает булево, заканчивается ли строка от указанной строки


    .. py:staticmethod:: regionMatches(int ind1, String str, int ind2, int len)
    .. py:staticmethod:: regionMatches(boolean flag, int ind1, String str, int ind2, int len)


    .. py:method:: toCharArray()

        возвращает массив символово из строки

    
    .. py:method:: charAt(int index)

        возвращает символ из строки

    
    .. py:method:: toLowerCase()
    .. py:method:: toLowerCase(Locale loc)

        возвращает новую строку, с нижним регистром символов

    
    .. py:method:: toUpperCase()
    .. py:method:: toUpperCase(Locale loc)

        возвращает новую строку, с верхним регистром символов


    .. py:method:: replace(char old, char new)
    .. py:method:: replace(String old, String new)

        возвращает новую строку, с замененными символами, строками


    .. py:method:: replaceFirst(String old, String new)

        возвращает новую строку, с замененным символом одним символом


    .. py:method:: trim()

        возвращает новую строку, с удаленными пробелами сначала и конца

    .. py:staticmethod:: valueOf(Boolean vool)
    .. py:staticmethod:: valueOf(Char char)
    .. py:staticmethod:: valueOf(Integer int)
    .. py:staticmethod:: valueOf(Long long)
    .. py:staticmethod:: valueOf(Float float)
    .. py:staticmethod:: valueOf(Double double)
    .. py:staticmethod:: valueOf(Char[] char)
    .. py:staticmethod:: valueOf(Object obj)
    .. py:staticmethod:: valueOf(Char[] char, int offset, int len)