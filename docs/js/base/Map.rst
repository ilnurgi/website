Map, WeakMap - коллекция пар ключ-значение
==========================================

Map
---

.. note:: EcmaScript6

.. py:class:: Map()

    .. code-block:: js

        let map = new Map();
        let map2 = new Map([[1, 2], [3, 4]]);


    .. py:attribute:: size

        Количесвто ключей в коллекции

        .. code-block:: js

            map2.size;
            // 2


    .. py:function:: clear()

        Очищает коллекцию

        .. code-block:: js

            map.clear();


    .. py:function:: delete(key)

        Удаляет пару ключ-значение из коллекции

        .. code-block:: js

            map.delete("2");


    .. py:function:: get(key)

        Возвращает значение по ключу

        .. code-block:: js

            map.get("2");


    .. py:function:: has(key)

        Проверяет, есть ли ключ в коллекции

        .. code-block:: js

            map.has("2");
            // false


    .. py:function:: set(key, value)

        Добавляет ключ и значение

        .. code-block:: js

            let o = {n: '1'};
            map.set(o, "A");


WeakMap
-------

.. note:: EcmaScript6

Аналогичен :py:class:`Map`, но имеет отличия:

* ключи могут быть только ссылками на объекты

* если нет другой ссылки на объект ключа в коллекции, то ключ уничтожится сборщиком мусора

* коллекция не перечисляема

    * нельзя узнать размер

    * нельзя итерироваться


.. py:class:: WeakMap()

    .. code-block:: js

        let weakmap = WeakMap();


    .. py:function:: delete(key)

        Удаляет пару ключ-значение из коллекции

        .. code-block:: js

            map.delete("2");


    .. py:function:: get(key);

        Возвращает значение по ключю

        .. code-block:: js

            map.get("2");


    .. py:function:: set(key, value)

        Добавляет ключ и значение

        .. code-block:: js

            let o = {n: '1'};
            map.set(o, "A");