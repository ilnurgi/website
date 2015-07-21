.. py:module:: java.util

AbstratctList
====

Этот класс расширяет :py:class::`java.util.AbstractCollection` и реализует интерфейс List.

Для реализации создания не модифицируемого списка необходимо имплементировать
методы `public Object get(int index)` и `public int size()`. 

Для реализации модифицируемого списка необходимо так же реализовать метод `public void set(int index, Object element)` (в противном случае, при его вызове будет возбуждено исключение UnsupportedOperationException)

В отличии от AbstractCollection в этом случае нет необходимости реализовывать метод `iterator`, т.к. он уже реализован поверх методов доступа к элементам списка get, set, add, remove.


.. py:class:: AbstratctList()

    Наследник :py:class::`java.util.AbstratctCollection`

    .. py:method:: get()
    .. py:method:: set()
    .. py:method:: indexOf()
    .. py:method:: lastIndexOf()
    .. py:method:: listIterator()
    .. py:method:: subList()
    .. py:method:: equals()
    .. py:method:: hashCode()
    .. py:method:: removeRange()