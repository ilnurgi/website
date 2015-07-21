.. py:module:: java.util

AbstratctCollection
====

Этот класс реализует все методы определенные в интерфейсе :py:class::`java.util.Collection` за исключением iterator и size, т.о. для того что бы создать не модифицируемую коллекцию нужно переопределить эти методы.

Для реализации модифицируемой коллекции, необходимо еще переопределить метод `public void add(Object o)` (в противном случае, при его вызове будет возбуждено исключение UnsupportedOperationException).

Необходимо так же определить два конструктора без аргументов и с аргументом Collection.
Первый должен создавать пустую коллекцию, второй коллекцию на основе сеуществующей.


.. py:class:: AbstratctCollection()

    .. py:method:: iterator()
    .. py:method:: size()
    .. py:method:: isEmpty()
    .. py:method:: contains()
    .. py:method:: toArray()
    .. py:method:: add()
    .. py:method:: remove()
    .. py:method:: containsAll()
    .. py:method:: addAll()
    .. py:method:: removeAll()
    .. py:method:: retainAll()
    .. py:method:: clear()
    .. py:method:: toString()