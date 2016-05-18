Symbol - символ
===============

.. note:: ECMAScript6


.. js:class:: Symbol()

    .. code-block:: js

        var s = Symbol();
        typeof s;
        // 'symbol'

    .. code-block:: js

        try {
            let s = new Symbol();
        } catch (e) {
            // Symbol is not a constructor
        }


    .. js:attribute:: hasInstance

    .. js:attribute:: isContcatSpreadable

    .. js:attribute:: iterator

    .. js:attribute:: match

    .. js:attribute:: replace

    .. js:attribute:: search

    .. js:attribute:: species

    .. js:attribute:: split

    .. js:attribute:: toPrimitive

    .. js:attribute:: toStringTag
    
    .. js:attribute:: unscopables

    .. js:function:: for(string)

        Создает символ глобально

        .. note:: ECMAScript6