.. py:module:: tkinter

Entry
=====

Виджет, поле ввода одно-строчного текста


.. py:class:: Entry(**kwargs)

    Наследник :py:class:`Widget`, :py:class:`XView`

    * bd - ширина границы
    * exportselection -
    * insertbackground -
    * insertborderwidth -
    * insertofftime -
    * insertontime -
    * insertwidth -
    * invalidcommand -
    * invcmd -
    * selectbackground - строка, цвет фона выделенного текста
    * selectborderwidth - строка, ширина границы выделенного текста
    * selectforeground - строка, цвет выделенного текста
    * show - строка, которая заменяет вводимые символы, например для пароля
    * state -
    * validate -
    * validatecommand -
    * vcmd -
    * width - ширина элемента в знакоместах
    * xscrollcommand -

    .. code-block:: py

        entry = Entry(parent)


    .. py:method:: get()

        Возвращает текст виджета


    .. py:method:: delete(first, last=None)

        Очищает поле ввода от и до указанной позиции :ref:`const_insert_mark`


    .. py:method:: icursor(index)

        Перемещает курсор на указанную позицию


    .. py:method:: index(index)

        Возвращает позицию курсора


    .. py:method:: insert(index, string)

        Вставляет текст в поле, по указанной позиции


    .. py:method:: select_adjust(index)
    .. py:method:: selection_adjust(index)

        Возвращает булево, индекс находится в выборе


    .. py:method:: select_clear()
    .. py:method:: selection_clear()

        Убирает выделение


    .. py:method:: select_from(index)
    .. py:method:: selection_from(index)

        Устанавливает начальную позицию для выбора


    .. py:method:: select_present()
    .. py:method:: selection_present()

        Возвращает булево, имеется ли выделение в виджете


    .. py:method:: select_range(start, end)
    .. py:method:: selection_range(start, end)

        Выделяет указанный диапазон


    .. py:method:: select_to(index)
    .. py:method:: selection_to(index)

        Выделяет до указанной позиции




