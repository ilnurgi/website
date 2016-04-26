CustomEvent - конструктор своих событий
=======================================

.. js:class:: CustomEvent()

    .. code-block:: js

        var evt = new CustomEvent('eventtype');

        window.addEventListener('eventtype', function(){...});

        // запускаем евент
        window.dispatchEvent(evt);


    .. js:function:: initCustomEvent()

        .. code-block:: js

            evt.initCustomEvent('eventtype', false, false, {});