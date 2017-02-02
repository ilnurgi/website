LocalStorage - key-value хранилище
==================================

Данное хранилище работает для домена


.. py:class:: LocalStorage()

    .. py:function:: getItem(key)

        Возвращает значение по ключу

        .. code-block:: js

            localStorage.getItem("key");
            localStorage.key2;
            localStorage['key3'];


    .. py:function:: setItem(key, value)

        Устанавливает новый ключ и значение в хранилище

        .. code-block:: js

            localStorage.setItem("key", "value");
            localStorage.key2 = 'value2';
            localStorage['key3'] = 'value3';


    