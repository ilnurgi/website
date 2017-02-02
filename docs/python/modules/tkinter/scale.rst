.. py:module:: tkinter

Scale - виджет, шкала выбора
============================


.. py:class:: Scale(**kwargs)

    виджет, шкала выбора

    Наследник :py:class:`Widget`

    * `command` - обработчик изменения значения виджета
    * `digits` -
    * `from` - начальная позиция
    * `label` - подпись виджета
    * `length` - длина бегунка
    * `orient` - константа :ref:`const_orient`
    * `repeatdelay` -
    * `repeatinterval` -
    * `resolution` - шаг
    * `showvalue` -
    * `sliderlength` - длина бегунка
    * `sliderrelief` -
    * `state` -
    * `tickinterval` - градуировка бегунка
    * `to` - конечная позиция
    * `troughcolor` -
    * `variable` -
    * `width` -


    .. py:method:: coords(value=None)

        Возвращает кортеж (х, у) положение слайдера относительно шкалы.


    .. py:method:: get()

        Возвращает текущее значение


    .. py:method:: identify(x, y)

        Возвращает значение, соответсвующее указанной позиции


    .. py:method:: set(value)

        Утсанавливает текущее значение