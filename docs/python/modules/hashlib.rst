.. py:module:: hashlib

hashlib - шифрование строк
==========================

.. py:class:: HASH

    .. py:method:: digest()

        возвращает строку (в 3 питоне зашифрованную последовательность байтов)

    .. py:method:: hesdigest(str)

        возвращает строку

    .. py:method:: update(str)

        присоединяет новый обхект к текущему значению


.. py:method:: md5(str)
    
    Шифрует объект по алгоритму MD5 и возвращает объект _hashlib.HASH

.. py:method:: sha1(str)
.. py:method:: sha224(str)
.. py:method:: sha256(str)
.. py:method:: sha384(str)
.. py:method:: sha512(str)