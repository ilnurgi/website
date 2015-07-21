.. py:module:: java.io

ByteArrayOutputStream - поток, записывающий данные в массив байт
===============================================


.. py:class:: ByteArrayOutputStream()

    Наследник :py:class::`java.io.OutputStream`


    .. py:method:: toByteArray()

        Возвращает записанные в массив данные

    ::

        ByteArrayOutputStream out = new ByteArrayOutputStream();
        out.write(10);
        out.write(11);
        byte[] bytes = out.toByteArray(); // [10, 11]