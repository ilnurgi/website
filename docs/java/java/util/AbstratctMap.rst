.. py:module:: java.util

AbstratctMap
====

Этот класс расширяет реализует основную функциональность определенную в интерфейсе Map 

Для реализации не модифицируемого класса, унаследованного от AbstractMap достаточно определить метод entrySet, который должен возвращать объект приводимый к типу AbstractSet. Этот набор (Set) не должен обеспечивать методов для добавления у даления элементов из набора. 

Для реализации модифицируемого класса Map необходимо так же переопределить метод put и итератор возвращаемый entrySet().iterator()


.. py:class:: AbstratctMap()

    .. py:method:: size()
    .. py:method:: isEmpty()
    .. py:method:: containsValue()
    .. py:method:: containsKey()
    .. py:method:: get()
    .. py:method:: put()
    .. py:method:: remove()
    .. py:method:: putAll()
    .. py:method:: clear()
    .. py:method:: keySet()
    .. py:method:: values()
    .. py:method:: entrySet()
    .. py:method:: equals()
    .. py:method:: hashCode()
    .. py:method:: toString()