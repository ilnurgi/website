.. py:module:: java.lang

Boolean - объектная обертка для типа boolean
============================================


.. py:class:: Boolean()
.. py:class:: Boolean(String str)

    Реализует интерфейс :py:class::`java.lang.Comparable`, :py:class::`java.io.Serializable`

    ::

        Boolean b = new Boolean("true");


    .. py:method:: booleanValue()

        Значение


    .. py:method:: parseBoolean(String str)

        возвращает объект по аргументу


    .. py:staticmethod:: valueOf(boolean b)

        возвращает объект

        ::

            Boolean b = Boolean.valueOf(true);
            Boolean b = true;

