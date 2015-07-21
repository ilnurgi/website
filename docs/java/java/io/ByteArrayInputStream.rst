.. py:module:: java.io

ByteArrayInputStream - поток, считывающий данные из массива байт
===============================================


.. py:class:: ByteArrayInputStream()

    Наследник :py:class::`java.io.InputStream`

    ::

        byte[] bytes = {1,-1,0};
        ByteArrayInputStream in = new ByteArrayInputStream(bytes);
        int readedInt = in.read(); // readedInt=1
        readedInt = in.read(); // readedInt=255. Однако (byte)readedInt даст значение -1
        readedInt = in.read(); // readedInt=0