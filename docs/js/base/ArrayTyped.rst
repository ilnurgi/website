Типизированные массивы
======================

.. note:: EcmaScript6


DataView
--------

.. py:class:: ArrayTyped(size)

    .. note:: EcmaScript6    

    .. code-block:: js

        let buffer = new ArrayBuffer(80);
        let view = new DataView(buffer);
        view.setInt32(8, 22, false);
        view.getInt32(8, false);
        // 22

    .. py:method:: setInt8(offset, value, be)
    .. py:method:: setInt16(offset, value, be)
    .. py:method:: setInt32(offset, value, be)

        Использует 8/16/32 бит для хранения числа, принимает целое число со знаком

        * `offset` - количесвто байтов, которое следует отступить от начала массива перед чтением/записью числа.
        * `value` - записываемое число
        * `be` - порядок записи байтов байтов числа, false - старшие байты будут записаны первыми.


    .. py:method:: setUint8(offset, value, be)
    .. py:method:: setUint16(offset, value, be)
    .. py:method:: setUint32(offset, value, be)

        Использует 8/16/32 бит для хранения числа, принимает целое число без знака


    .. py:method:: setFloat32(offset, value, be)
    .. py:method:: setFloat64(offset, value, be)

        Использует 32/64 бит для хранения числа, принимает вещественное число со знаком


    .. py:method:: getInt8(offset, be)
    .. py:method:: getInt16(offset, be)
    .. py:method:: getInt32(offset, be)

        Читает 8/16/32 бит и возвращает целое число со знаком


    .. py:method:: getUint8(offset, be)
    .. py:method:: getUint16(offset, be)
    .. py:method:: getUint32(offset, be)

        Читает 8/16/32 бит и возвращает целое число без знака

    .. py:method:: getFloat32(offset, be)
    .. py:method:: getFloat64(offset, be)

        Читает 32/64 бит и возвращает вещественное число со знаком


Float64Array
------------

Буферный массив 64-битных вещественных чисел

.. py:class:: Float64Array(buffer)
    
    .. note:: EcmaScript6

    .. code-block:: js

        // создаем буферный массив на 640 бит, 80 * 8
        let buffer = new ArrayBuffer(80);

        // создаем типизированный буфер 64 битных чисел
        // в буфере можно хранить не более 10 числе, 640/64
        let typed_array = new Float64Array(buffer);
        typed_array[4] = 11;
        
        typed_array.length;
        // 10

        typed_array[4];
        // 11


Int8Array, Int16Array, Int32Array
---------------------------------

Буферный массив для 8/16/32 битных чисел со знаком

.. py:class:: Int8Array(buffer)

    .. note:: EcmaScript6


.. py:class:: Int16Array(buffer)

    .. note:: EcmaScript6


.. py:class:: Int32Array(buffer)

    .. note:: EcmaScript6


Uint8Array, Uint16Array, Uint32Array
------------------------------------

Буферный массив для 8/16/32 битных чисел без знака

.. py:class:: Uint8Array(buffer)

    .. note:: EcmaScript6


.. py:class:: Uint16Array(buffer)

    .. note:: EcmaScript6


.. py:class:: Uint32Array(buffer)

    .. note:: EcmaScript6


Float32Array, Float64Array
--------------------------

Буферный массив для 32/64 битных вещественных чисел со знаком

.. py:class:: Float32Array(buffer)

    .. note:: EcmaScript6


.. py:class:: Float64Array(buffer)

    .. note:: EcmaScript6
