.. py:module:: tkinter

Базовые объекты
===============

Основные методы виджетов
------------------------

.. py:method:: bell()

    Издает звук

.. py:method:: bind(event, callback)

    Привязывает событие виджета к обработчику. Передает в обработчик в качестве аргумента. объект :py:class::`tkinter.Event`

    >>> widget.bind('<Button-1>', callback)
    
    * Button-1 - нажатие левой кнопки мыши
    * Button-2 - нажатие средней кнопки мыши
    * Button-3 - нажатие правой кнопки мыши
    * Double-Button-1 - двойное нажатие
    * ButtonRelease-1 - отпускание кнопки
    * B1-Motion - движение мыши с зажатой кнопкой
    * Enter - наведение курсора на тег
    * Leave - уход курсора от тега
    * r - кнопка на клавиатуре
    * Shift_L - левый шифт
    * Alt_L
    * Control_R
    * Return
    * Caps_Lock
    * Escape
    * Prior - PageUp
    * Next- PageDown.
    * Up
    * Down
    * Left 
    * Right

.. py:method:: destroy()

    Уничтожает виджет

    >>> window.destroy()


.. py:method:: focus()

    Устанавливает фокус на виджете

.. py:method:: get()

    Возвращает значение виджета

.. py:method:: protocol(event, func)

    Вещает обработчик события виджета

    :param event: ивент, ('WM_DELETE_WINDOW')
    :param func: обработчик

.. py:method:: set()

    Устанавливает значение виджета

.. py:method:: tag_bind(tag, event, callback)

    Привязывает обработчик тега с ивентом