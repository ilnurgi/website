Map, WeakMap - коллекция пар ключ-значение
==========================================

Map
---

.. note:: EcmaScript6

.. js:class:: Map()

    .. code-block:: js

        let map = new Map();
        let map2 = new Map([[1, 2], [3, 4]]);


    .. js:attribute:: size

        Количесвто ключей в коллекции

        .. code-block:: js

            map2.size;
            // 2


    .. js:function:: clear()

        Очищает коллекцию

        .. code-block:: js

            map.clear();


    .. js:function:: delete(key)

        Удаляет пару ключ-значение из коллекции

        .. code-block:: js

            map.delete("2");


    .. js:function:: get(key)

        Возвращает значение по ключу

        .. code-block:: js

            map.get("2");


    .. js:function:: has(key)

        Проверяет, есть ли ключ в коллекции

        .. code-block:: js

            map.has("2");
            // false


    .. js:function:: set(key, value)

        Добавляет ключ и значение

        .. code-block:: js

            let o = {n: '1'};
            map.set(o, "A");


WeakMap
-------

.. note:: EcmaScript6

Аналогичен :js:class:`Map`, но имеет отличия:

* ключи могут быть только ссылками на объекты

* если нет другой ссылки на объект ключа в коллекции, то ключ уничтожится сборщиком мусора

* коллекция не перечисляема

    * нельзя узнать размер

    * нельзя итерироваться


.. js:class:: WeakMap()

    .. code-block:: js

        let weakmap = WeakMap();


    .. js:function:: delete(key)

        Удаляет пару ключ-значение из коллекции

        .. code-block:: js

            map.delete("2");


    .. js:function:: get(key);

        Возвращает значение по ключю

        .. code-block:: js

            map.get("2");


    .. js:function:: set(key, value)

        Добавляет ключ и значение

        .. code-block:: js

            let o = {n: '1'};
            map.set(o, "A");