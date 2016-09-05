.. py:module:: tkinter

Checkbutton
===========

Виджет, галка


.. py:class:: Checkbutton(**kwargs)

    Виджет, флажок

    Наследник :py:class:`Widget`

    * `command` - обработчик изменения состояния виджета
    * `disabledforeground` - цвет текста, для выключенного виджета
    * `height` - число, количество строк текста виджета
    * `image` - картинка виджета
    * `indicatoron` -
    * `offvalue` - значение для не отмеченного виджета, по умолчанию 0
    * `onvalue` - значение для отмеченного (checked) виджета, по умолчанию 1
    * `selectcolor` - цвет отмеченного виджета
    * `selectimage` - картинка для отмеченного виджета
    * `state` - состояние виджета
    * `text` - текст
    * `variable` - :py:class:`IntVar`, переменная
    * `width` - ширина виджета

    .. code-block:: py

        check_button = Checkbutton(
            master,
            text="Some text",
            command=lambda: pass
        )


    .. py:method:: deselect()

        Переводит виджет в состояние не выбран


    .. py:method:: flash()



    .. py:method:: invoke()

        Возвращает результат обработчика виджета


    .. py:method:: select()

        Переводит виджет в состояние выбран


    .. py:method:: toggle()

        Изменяет текущее состояние выбран/не выбран на противоположное