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

.. py:method:: config(**kwargs)

    Конфигурирует виджет

    :param str bg: цвет фона
    :param func command: обработчик
    :param str cursor: тип курсора при наведении (pencil, cross, watch, hand2)
    :param str fg: цвет текста
    :param str font: шрифт, 'Helvetica 20 italic', (bold, italic, underline, overstrike, roman, normal)
    :param justify: выравнивание текста (tk.LEFT, tk.RIGHT, tk.CENTER)
    :param int height: высота
    :param int width: ширина
    :param relief: стиль отображения виджета, tk.SOLID, tk.SUNKEN, tk.FLAT, tk.RIDGE, tk.RAISED, tk.GROOVE.
    :param state: tk.NORMAL, tk.ACTIVE, tk.DISABLED, 'readonly'
    :param func yscrollcommand: обработчик
    :param func xscrollcommand: обработчик


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

Основные методы расположения виджетов
-------------------------------------

.. py:method:: widget.pack(**kwargs)

    :param side: расположение, tk.TOP, tk.BOTTOM, tk.LEFT, tk.RIGHT
    :param fill: растягивание, tk.X, tk.Y, tk.BOTH
    :param expand: устанавливает параметры растягивания при изменении окна, tk.YES
    :param anchor: расположение виджета в виджете, tk.N, rk.S, tk.W, tk.E
    :param padx: внутренний отступ виджета
    :param pady: внутренний отступ виджета


.. py:method:: widget.grid(**kwargs)

    :param row: номер строки
    :param column: номер колонки


.. py:method:: widget.place(x, y)

PhotoImage
==========

.. py:class:: PhotoImage(file)

    Возвращает объект изображение, которое можно вставить в виджеты