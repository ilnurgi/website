.. py:module:: java.util

AbstratctSequentialList
====

Этот класс расширяет AbstractList и является основой для класса LinkedList. 

Основное отличие от AbstractList заключается в том, что этот класс обеспечивает не только последовательный, но и произвольный доступ к элементам списка, с помощью методов get(int index), set(int index, Object element), set(int index, Object element), add(int index, Object element) и remove(int index). 

Для того что бы реализовать данный класс необходимо переопределить методы listIterator и size. Причем если реализуется не модифицируемый список, для итератора достаточно реализовать методы hasNext, next, hasPrevious, previous и index. 

Для модифицируемого списка необходимо дополнительно реализовать метод set, а для списков переменной длинны еще и add и remove.


.. py:class:: AbstratctSequentialList()

    Наследник :py:class::`java.util.AbstratctList`