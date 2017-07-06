.. py:module:: tkinter

Button
======

Виджет, кнопка


.. py:class:: Button(**kwargs)

     Наследник :py:class:`Widget`

    * background - :py:class:`str`, цвет фона
    * bg - :py:class:`str`, цвет фона
    * command - ссылка на функцию обработчика
    * compound
    * default
    * fg - :py:class:`str`, цвет текста
    * height - :py:class:`int`, высота виджета, количесвто строк - для обычной кнопки, пиксели - для кнопки картинки
    * image - кнопка-картинка
    * overrelief
    * state - константа :ref:`const_state`
    * text - :py:class:`str`, текст надписи на кнопке
    * width - :py:class:`str`, ширина виджета, количесвто символов - для обычной кнопки, пиксели - для кнопки картинки

    .. code-block:: py

        button = Button(
            master,
            text="some text",
            command=lambda: pass,
            image=PhotoImage(),
        )

    .. code-block:: py

        button = Button(master)
        button["text"] = "Some text"
        button.bind("<Button-1>", lambda event: pass)


    .. py:method:: flash()

        Вспышка кнопки, чередование активной и нормальной цветов.


    .. py:method:: invoke()

        Возвращает результат работы обработчика кнопки

    .. py:method:: pack(side)

        Распологает виджет на родительском виджете

        * side

            * :py:attr:`tkinter.LEFT`
            * :py:attr:`tkinter.RIGHT`

        .. code-block:: py

            button.pack(side=LEFT)
