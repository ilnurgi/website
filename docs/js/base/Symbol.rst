Symbol - символ
===============

.. note:: ECMAScript6


.. py:class:: Symbol()

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


    .. py:attribute:: hasInstance

    .. py:attribute:: isContcatSpreadable

    .. py:attribute:: iterator

    .. py:attribute:: match

    .. py:attribute:: replace

    .. py:attribute:: search

    .. py:attribute:: species

    .. py:attribute:: split

    .. py:attribute:: toPrimitive

    .. py:attribute:: toStringTag
    
    .. py:attribute:: unscopables

    .. py:function:: for(string)

        Создает символ глобально

        .. note:: ECMAScript6