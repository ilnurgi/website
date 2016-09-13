SessionStorage - key-value хранилище
====================================

Данные хранилища перезаписываются после окончания сессии,
напрмер после закрытия вкладки.

.. py:class:: SessionStorage()


    .. py:function:: getItem(key)

        Возвращает значение по ключу

        .. code-block:: js

            sessionStorage.getItem("key");
            sessionStorage.key2;
            sessionStorage['key3'];


    .. py:function:: setItem(key, value)

        Устанавливает новый ключ и значение в хранилище

        .. code-block:: js

            sessionStorage.setItem("key", "value");
            sessionStorage.key2 = 'value2';
            sessionStorage['key3'] = 'value3';


    