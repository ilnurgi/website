CustomEvent - конструктор своих событий
=======================================

.. py:class:: CustomEvent()

    .. code-block:: js

        var evt = new CustomEvent('eventtype');

        window.addEventListener('eventtype', function(){...});

        // запускаем евент
        window.dispatchEvent(evt);


    .. py:function:: initCustomEvent()

        .. code-block:: js

            evt.initCustomEvent('eventtype', false, false, {});