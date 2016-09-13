DataView
========

Реализует чтение/запись значений в ArrayBuffer   


.. py:class:: DataView(ArrayBuffer buffer, [byteOffset], [byteLength])

    Наследнк :py:class:`ArrayBufferView`


    .. py:method:: getFloat32(byteOffset, [littleEndian])

        Ин­тер­пре­ти­ру­ет 4 бай­та, на­чи­ная с по­зи­ции byteOffset,
        как ве­ще­ст­вен­ное чис­ло и воз­вра­ща­ет его.


    .. py:method:: getFloat64(byteOffset, [littleEndian])

        Ин­тер­пре­ти­ру­ет 8 бай­тов, на­чи­ная с по­зи­ции byteOffset,
        как ве­ще­ст­вен­ное чис­ло и воз­вра­ща­ет его.


    .. py:method:: getInt16(byteOffset, [littleEndian])

        Ин­тер­пре­ти­ру­ет 2 бай­та, на­чи­ная с по­зи­ции byteOffset,
        как це­лое чис­ло со зна­ком и воз­вра­ща­ет его.


    .. py:method:: getInt32(byteOffset, [littleEndian])
        
        Ин­тер­пре­ти­ру­ет 4 бай­та, на­чи­ная с по­зи­ции byteOffset,
        как це­лое чис­ло со зна­ком и воз­вра­ща­ет его.


    .. py:method:: getInt8(byteOffset)
        
        Ин­тер­пре­ти­ру­ет байт в по­зи­ции byteOffset,
        как це­лое чис­ло со зна­ком и воз­вра­ща­ет его.


    .. py:method:: getUint16(byteOffset,[littleEndian])
        
        Ин­тер­пре­ти­ру­ет 2 бай­та, на­чи­ная с по­зи­ции byteOffset,
        как це­лое чис­ло без зна­ка и воз­вра­ща­ет его.


    .. py:method:: getUint32(byteOffset, [littleEndian])
        
        Ин­тер­пре­ти­ру­ет 4 бай­та, на­чи­ная с по­зи­ции byteOffset,
        как це­лое чис­ло без зна­ка и воз­вра­ща­ет его.


    .. py:method:: getUint8(byteOffset)
        
        Ин­тер­пре­ти­ру­ет байт в по­зи­ции byteOffset,
        как це­лое чис­ло без зна­ка и воз­вра­ща­ ет его


    .. py:method:: setFloat32(byteOffset, float value, [littleEndian])
        
        Пре­об­ра­зу­ет зна­че­ние value в 4-бай­то­вое ве­ще­ст­вен­ное пред­став­ле­ние и
        за­пи­сы­вает по­лу­чен­ные бай­ты в бу­фер, на­чи­ная с по­зи­ции byteOffset.


    .. py:method:: setFloat64(byteOffset, value, [littleEndian])
    
        Пре­об­ра­зу­ет зна­че­ние value в 8-бай­то­вое ве­ще­ст­вен­ное пред­став­ле­ние и
        за­пи­сы­ва­ет по­лу­чен­ные бай­ты в бу­фер, на­чи­ная с по­зи­ции byteOffset.


    .. py:method:: setInt16(byteOffset, short value, [littleEndian])
    
        Пре­об­ра­зу­ет зна­че­ние value в 2-бай­то­вое це­ло­чис­лен­ное пред­став­ле­ние и
        за­пи­сы­ва­ет по­лу­чен­ные бай­ты в бу­фер, на­чи­ная с по­зи­ции byteOffset.


    .. py:method:: setInt32(byteOffset, long value, [littleEndian])

        Пре­об­ра­зу­ет зна­че­ние value в 4-бай­то­вое це­ло­чис­лен­ное пред­став­ле­ние и
        за­пи­сы­ва­ет по­лу­чен­ные бай­ты в бу­фер, на­чи­ная с по­зи­ции byteOffset.


    .. py:method:: setInt8(byteOffset, value)
    
        Пре­об­ра­зу­ет зна­че­ние value в 1-бай­то­вое це­ло­чис­лен­ное пред­став­ле­ние и
        за­пи­сы­ва­ет по­лу­чен­ный байт в бу­фер, в по­зи­цию byteOffset.


    .. py:method:: setUint16(byteOffset, value, [littleEndian])
    
        Пре­об­ра­зу­ет зна­че­ние value в 2-бай­то­вое це­ло­чис­лен­ное пред­став­ле­ние
        без зна­ка и за­пи­сы­ва­ет по­лу­чен­ные бай­ты в бу­фер,
        на­чи­ная с по­зи­ции byteOffset.

    .. py:method:: setUint32(byteOffset, value, [littleEndian])
    
        Пре­об­ра­зу­ет зна­че­ние value в 4-бай­то­вое це­ло­чис­лен­ное пред­став­ле­ние
        без зна­ка и за­пи­сы­ва­ет по­лу­чен­ные бай­ты в бу­фер,
        на­чи­ная с по­зи­ции byteOffset.


    .. py:method:: setUint8(byteOffset, value)
    
        Пре­об­ра­зу­ет зна­че­ние value в 1-бай­то­вое це­ло­чис­лен­ное пред­став­ле­ние
        без зна­ка и за­пи­сы­ва­ет по­лу­чен­ный байт в бу­фер в по­зи­цию byteOffset.