DataView - реализует чтение/запись значений в ArrayBuffer   
=========================================================


.. js:class:: DataView(ArrayBuffer buffer, [byteOffset], [byteLength])

    Наследнк :js:class:`ArrayBufferView`


    .. js:function:: getFloat32(byteOffset, [littleEndian])

        Ин­тер­пре­ти­ру­ет 4 бай­та, на­чи­ная с по­зи­ции byteOffset, как ве­ще­ст­вен­ное чис­ло и воз­вра­ща­ет его.


    .. js:function:: getFloat64(byteOffset, [littleEndian])

        Ин­тер­пре­ти­ру­ет 8 бай­тов, на­чи­ная с по­зи­ции byteOffset, как ве­ще­ст­вен­ное чис­ло и воз­вра­ща­ет его.


    .. js:function:: getInt16(byteOffset, [littleEndian])

        Ин­тер­пре­ти­ру­ет 2 бай­та, на­чи­ная с по­зи­ции byteOffset, как це­лое чис­ло со зна­ком и воз­вра­ща­ет его.


    .. js:function:: getInt32(byteOffset, [littleEndian])
        
        Ин­тер­пре­ти­ру­ет 4 бай­та, на­чи­ная с по­зи­ции byteOffset, как це­лое чис­ло со зна­ком и воз­вра­ща­ет его.


    .. js:function:: getInt8(byteOffset)
        
        Ин­тер­пре­ти­ру­ет байт в по­зи­ции byteOffset, как це­лое чис­ло со зна­ком и воз­вра­ща­ет его.


    .. js:function:: getUint16(byteOffset,[littleEndian])
        
        Ин­тер­пре­ти­ру­ет 2 бай­та, на­чи­ная с по­зи­ции byteOffset, как це­лое чис­ло без зна­ка и воз­вра­ща­ет его.


    .. js:function:: getUint32(byteOffset, [littleEndian])
        
        Ин­тер­пре­ти­ру­ет 4 бай­та, на­чи­ная с по­зи­ции byteOffset, как це­лое чис­ло без зна­ка и воз­вра­ща­ет его.


    .. js:function:: getUint8(byteOffset)
        
        Ин­тер­пре­ти­ру­ет байт в по­зи­ции byteOffset, как це­лое чис­ло без зна­ка и воз­вра­ща­ ет его


    .. js:function:: setFloat32(byteOffset, float value, [littleEndian])
        
        Пре­об­ра­зу­ет зна­че­ние value в 4-бай­то­вое ве­ще­ст­вен­ное пред­став­ле­ние и за­пи­сы­ва­ ет по­лу­чен­ные бай­ты в бу­фер, на­чи­ная с по­зи­ции byteOffset.


    .. js:function:: setFloat64(byteOffset, value, [littleEndian])
    
        Пре­об­ра­зу­ет зна­че­ние value в 8-бай­то­вое ве­ще­ст­вен­ное пред­став­ле­ние и за­пи­сы­ва­ет по­лу­чен­ные бай­ты в бу­фер, на­чи­ная с по­зи­ции byteOffset.


    .. js:function:: setInt16(byteOffset, short value, [littleEndian])
    
        Пре­об­ра­зу­ет зна­че­ние value в 2-бай­то­вое це­ло­чис­лен­ное пред­став­ле­ние и за­пи­сы­ва­ет по­лу­чен­ные бай­ты в бу­фер, на­чи­ная с по­зи­ции byteOffset.


    .. js:function:: setInt32(byteOffset, long value, [littleEndian])

        Пре­об­ра­зу­ет зна­че­ние value в 4-бай­то­вое це­ло­чис­лен­ное пред­став­ле­ние и за­пи­сы­ва­ет по­лу­чен­ные бай­ты в бу­фер, на­чи­ная с по­зи­ции byteOffset.


    .. js:function:: setInt8(byteOffset, value)
    
        Пре­об­ра­зу­ет зна­че­ние value в 1-бай­то­вое це­ло­чис­лен­ное пред­став­ле­ние и за­пи­сы­ва­ет по­лу­чен­ный байт в бу­фер, в по­зи­цию byteOffset.


    .. js:function:: setUint16(byteOffset, value, [littleEndian])
    
        Пре­об­ра­зу­ет зна­че­ние value в 2-бай­то­вое це­ло­чис­лен­ное пред­став­ле­ние без зна­ка и за­пи­сы­ва­ет по­лу­чен­ные бай­ты в бу­фер, на­чи­ная с по­зи­ции byteOffset.

    .. js:function:: setUint32(byteOffset, value, [littleEndian])
    
        Пре­об­ра­зу­ет зна­че­ние value в 4-бай­то­вое це­ло­чис­лен­ное пред­став­ле­ние без зна­ка и за­пи­сы­ва­ет по­лу­чен­ные бай­ты в бу­фер, на­чи­ная с по­зи­ции byteOffset.


    .. js:function:: setUint8(byteOffset, value)
    
        Пре­об­ра­зу­ет зна­че­ние value в 1-бай­то­вое це­ло­чис­лен­ное пред­став­ле­ние без зна­ка и за­пи­сы­ва­ет по­лу­чен­ный байт в бу­фер в по­зи­цию byteOffset.