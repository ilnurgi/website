.. py:module:: tkinter

Button - виджет кнопка
======================


.. py:class:: Button(**kwargs)

    Кнопка, виджет.

    Наследник :py:class:`Widget`

    * background, bg - цвет фона
    * `command` - ссылка на функцию обработчика
    * `compound`
    * `default`
    * fg - цвет текста
    * `height` - число, высота виджета, количесвто строк - для обычной кнопки, пиксели - для кнопки картинки
    * `image` - кнопка-картинка
    * `overrelief`
    * `state` - константа :ref:`const_state`
    * `width` - число, ширина виджета, количесвто символов - для обычной кнопки, пиксели - для кнопки картинки

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
