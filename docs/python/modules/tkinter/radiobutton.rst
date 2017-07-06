.. py:module:: tkinter

Radiobutton
===========

Виджет, флажок


.. py:class:: Radiobutton(**kwargs)

    Наследник :py:class:`tkinter.Widget`

    * command - обработчик изменения состояния
    * height - высота виджета, выраженное в количествах строк
    * image - картинка виджета
    * indicatoron -
    * offvalue -
    * onvalue -
    * selectcolor - строка, цвет выбранного виджета
    * selectimage - картинка выбранного виджета
    * state -
    * text - :py:class:`str`, текст виджета
    * underline -
    * value - значение
    * variable - переменная значения
    * width -

    .. code-block:: py

        rbutton = RadioButton(parent, text='some text', variable=var, value=1)

    .. py:method:: deselect()

        Очищает от выбора виджет


    .. py:method:: flash()


    .. py:method:: invoke()

        Возвращает результат обработчика


    .. py:method:: select()

        Активирует виджет
