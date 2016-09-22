.. py:module:: binascii

binascii
========

Позволяет конвертировать данные в бинарный вид и в различные предлставления строк.

hexlify
-------

.. py:method:: hexlify()

    .. code-block:: py

        hexlify(b'\x89PNG\r\n\x1a\n')
        # b'89504e470d0a1a0a'


unhexlify
---------

.. py:method:: unhexlify()

    .. code-block:: py

        unhexlify(b'89504e470d0a1a0a')
        # b'\x89PNG\r\n\x1a\n'