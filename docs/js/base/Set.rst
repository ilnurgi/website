Set, WeakSet - коллекция уникальных типов любого типа
=====================================================

Set
---

.. py:class:: Set()

    .. note:: EcmaScript6

    .. code-block:: js

        let set1 = Set();
        let set2 = Set('Ilnurgi!!!');


    .. py:attribute:: size

        Размер множества

        .. code-block:: js

            set2.size;
            // 8


    .. py:function:: add(elem)

        Добавялет в множество элемент

        .. code-block:: js

            set2.add(12);


    .. py:function:: clear()

        Очищает множество от всех элементов.

        .. code-block:: js

            set2.clear()


    .. py:function:: delete(elem)

        Удаляет элемент из множества

        .. code-block:: js

            set2.delete(12);


    .. py:function:: has(elem)

        Имеет ли множество указанный объект

        .. code-block:: js

            set2.has('!');
            // true

WeakSet
-------

.. note:: EcmaScript6

Аналгоичен :py:class:`Set`, но имеет ряд отличий:

* может хранить только ссылки на объекты

* если нет других ссылок на объект, хранящийся в множестве, то объект удалится сборщиком мусора

* при создании объекта, ему нельзя передать итерируемый объект в качестве аргумента

* объект не является перечисляемым

    * нельзя узнать его длину

    * нельзя проитерироваться по нему


.. py:class:: WeakSet()

    .. code-block:: js

        let weakset = new WeakSet()

    
    .. py:function:: add(elem)

        Добавляет элемент в множество

        .. code-block:: js

            let a = {};
            weakset.add(a);