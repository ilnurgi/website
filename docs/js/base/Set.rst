Set, WeakSet - коллекция уникальных типов любого типа
=====================================================

Set
---

.. js:class:: Set()

    .. note:: EcmaScript6

    .. code-block:: js

        let set1 = Set();
        let set2 = Set('Ilnurgi!!!');


    .. js:attribute:: size

        Размер множества

        .. code-block:: js

            set2.size;
            // 8


    .. js:function:: add(elem)

        Добавялет в множество элемент

        .. code-block:: js

            set2.add(12);


    .. js:function:: clear()

        Очищает множество от всех элементов.

        .. code-block:: js

            set2.clear()


    .. js:function:: delete(elem)

        Удаляет элемент из множества

        .. code-block:: js

            set2.delete(12);


    .. js:function:: has(elem)

        Имеет ли множество указанный объект

        .. code-block:: js

            set2.has('!');
            // true

WeakSet
-------

.. note:: EcmaScript6

Аналгоичен :js:class:`Set`, но имеет ряд отличий:

* может хранить только ссылки на объекты

* если нет других ссылок на объект, хранящийся в множестве, то объект удалится сборщиком мусора

* при создании объекта, ему нельзя передать итерируемый объект в качестве аргумента

* объект не является перечисляемым

    * нельзя узнать его длину

    * нельзя проитерироваться по нему


.. js:class:: WeakSet()

    .. code-block:: js

        let weakset = new WeakSet()

    
    .. js:function:: add(elem)

        Добавляет элемент в множество

        .. code-block:: js

            let a = {};
            weakset.add(a);