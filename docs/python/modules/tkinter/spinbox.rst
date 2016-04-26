Spinbox - виджет, поле ввода с предустановленными вариантами
============================================================


.. py:class:: Spinbox(**kwargs)

    Виджет, поле ввода с предустановленными вариантами

    Наследник :py:class:`Widget`, :py:class:`XView`

    * `buttonbackground` -
    * `buttoncursor` -
    * `buttondownrelief` -
    * `buttonuprelief` -
    * `command` - обработчик изменения состояния
    * `disabledbackground` -
    * `disabledforeground` -
    * `format` -
    * `from` -
    * `invalidcommand` -
    * `increment` -
    * `readonlybackground` -
    * `state` -
    * `to` -
    * `validate` -
    * `validatecommand` -
    * `values` -
    * `width` -
    * `wrap` -


    .. py:method:: delete(first, last=None)

        Удаляет один или несколько элементов из виджета


    .. py:method:: get()

        Возвращает выбранное значение


    .. py:method:: identify(x, y)

        Возвращает название виджета по указанным координатам (none, buttondown, buttonup, entry)


    .. py:method:: index(index)

        Возвращает индекс по индексу


    .. py:method:: insert(index, s)

        Вставляет элемент по индексу


    .. py:method:: invoke(element)

        Возвращает результат обработку указанного элемента